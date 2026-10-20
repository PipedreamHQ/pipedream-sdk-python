"""Client assertions for private_key_jwt client authentication (RFC 7523).

An OAuth client that registered a public key authenticates at the token
endpoint with a short-lived JWT signed by the matching private key, instead of
a client secret. Requires the optional ``private-key`` extra:
``pip install "pipedream[private-key]"`` (PyJWT with cryptography).
"""

import asyncio
import datetime as dt
import json
import threading
import time
import typing
import uuid
from urllib.parse import urlsplit

import httpx
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .oauth_tokens.client import AsyncOauthTokensClient, OauthTokensClient
from .types.create_o_auth_token_response import CreateOAuthTokenResponse

CLIENT_ASSERTION_TYPE: typing.Literal["urn:ietf:params:oauth:client-assertion-type:jwt-bearer"] = (
    "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
)

# Assertions are single-use and only need to outlive one token request.
_ASSERTION_LIFETIME_SECONDS = 60
# Token requests authenticated with an assertion are retried here rather than
# by the HTTP client, so each attempt carries a newly signed assertion: the
# server rejects a reused one.
_MAX_RETRIES = 2
_TOKEN_BUFFER = dt.timedelta(minutes=2)


def issuer_from_base_url(base_url: str) -> str:
    """The API's issuer identifier: the base URL's origin, without a trailing slash."""
    parts = urlsplit(base_url)
    return f"{parts.scheme}://{parts.netloc}"


class ClientAssertionSigner:
    """Signs a new client assertion on every call to :meth:`sign`.

    The assertion is a JWT with ``iss`` and ``sub`` set to the client ID, the
    given ``aud``, a 60-second lifetime, and a random single-use ``jti``. The
    private key may be a PEM string (PKCS#8, PKCS#1, or SEC1) or a JWK as a JSON
    string; EC P-256 keys sign with ES256 and RSA keys with RS256. ``key_id``
    is sent as the ``kid`` header and defaults to the JWK's ``kid``, if any.
    The key is parsed and validated on construction.
    """

    def __init__(self, *, client_id: str, private_key: str, audience: str, key_id: typing.Optional[str] = None):
        try:
            import jwt  # noqa: F401  (PyJWT)
            from cryptography.hazmat.primitives.asymmetric import ec, rsa
        except ImportError as e:
            raise ImportError(
                'Authenticating with a private key requires the "private-key" extra: '
                'pip install "pipedream[private-key]"'
            ) from e

        self._client_id = client_id
        self._audience = audience
        self._key, jwk_kid = _load_private_key(private_key.strip())
        self._key_id = key_id or jwk_kid

        if isinstance(self._key, ec.EllipticCurvePrivateKey) and isinstance(self._key.curve, ec.SECP256R1):
            self._alg = "ES256"
        elif isinstance(self._key, rsa.RSAPrivateKey):
            self._alg = "RS256"
        else:
            raise ValueError("private_key must be an EC P-256 key (ES256) or an RSA key (RS256)")

    def sign(self) -> str:
        import jwt

        now = int(time.time())
        headers: typing.Dict[str, str] = {"typ": "client-authentication+jwt"}
        if self._key_id:
            headers["kid"] = self._key_id
        claims = {
            "iss": self._client_id,
            "sub": self._client_id,
            "aud": self._audience,
            "iat": now,
            "exp": now + _ASSERTION_LIFETIME_SECONDS,
            "jti": str(uuid.uuid4()),
        }
        return jwt.encode(claims, typing.cast(typing.Any, self._key), algorithm=self._alg, headers=headers)


def _load_private_key(text: str) -> typing.Tuple[typing.Any, typing.Optional[str]]:
    import jwt
    from cryptography.hazmat.primitives.serialization import load_pem_private_key

    try:
        if text.startswith("{"):
            jwk = json.loads(text)
            key = jwt.PyJWK(jwk).key
            kid = jwk.get("kid") if isinstance(jwk.get("kid"), str) else None
            if not hasattr(key, "sign"):
                raise ValueError("not a private key")
            return key, kid
        return load_pem_private_key(text.encode(), password=None), None
    except Exception as e:
        raise ValueError(
            "private_key must be a private key in PEM format or a JWK (JSON). "
            "If you passed a public key, pass the private key instead."
        ) from e


def _is_retryable(error: Exception) -> bool:
    # Rate limits, timeouts, connection failures, and server errors are
    # transient; 4xx errors such as invalid_client are not.
    if isinstance(error, (httpx.TimeoutException, httpx.TransportError)):
        return True
    if isinstance(error, ApiError):
        status = error.status_code
        return status is None or status in (408, 429) or status >= 500
    return False


def _expires_at(token: CreateOAuthTokenResponse) -> dt.datetime:
    return dt.datetime.now() + dt.timedelta(seconds=token.expires_in) - _TOKEN_BUFFER


class PrivateKeyJwtTokenProvider:
    """Retrieves and caches an OAuth access token, authenticating with client assertions."""

    def __init__(self, *, client_id: str, signer: ClientAssertionSigner, client_wrapper: SyncClientWrapper):
        self._client_id = client_id
        self._signer = signer
        self._auth_client = OauthTokensClient(client_wrapper=client_wrapper)
        self._access_token: typing.Optional[str] = None
        self._expires_at = dt.datetime.now()
        self._lock = threading.Lock()

    def get_token(self) -> str:
        if self._access_token and self._expires_at > dt.datetime.now():
            return self._access_token
        with self._lock:
            if self._access_token and self._expires_at > dt.datetime.now():
                return self._access_token
            token = self._request_token()
            self._access_token = token.access_token
            self._expires_at = _expires_at(token)
            return self._access_token

    def _request_token(self) -> CreateOAuthTokenResponse:
        attempt = 0
        while True:
            try:
                return self._auth_client.create(
                    client_id=self._client_id,
                    client_assertion_type=CLIENT_ASSERTION_TYPE,
                    client_assertion=self._signer.sign(),
                    request_options={"max_retries": 0},
                )
            except Exception as e:
                if attempt >= _MAX_RETRIES or not _is_retryable(e):
                    raise
                time.sleep(0.5 * 2**attempt)
                attempt += 1


class AsyncPrivateKeyJwtTokenProvider:
    """Async variant of :class:`PrivateKeyJwtTokenProvider`."""

    def __init__(self, *, client_id: str, signer: ClientAssertionSigner, client_wrapper: AsyncClientWrapper):
        self._client_id = client_id
        self._signer = signer
        self._auth_client = AsyncOauthTokensClient(client_wrapper=client_wrapper)
        self._access_token: typing.Optional[str] = None
        self._expires_at = dt.datetime.now()
        self._lock = asyncio.Lock()

    async def get_token(self) -> str:
        if self._access_token and self._expires_at > dt.datetime.now():
            return self._access_token
        async with self._lock:
            if self._access_token and self._expires_at > dt.datetime.now():
                return self._access_token
            token = await self._request_token()
            self._access_token = token.access_token
            self._expires_at = _expires_at(token)
            return self._access_token

    async def _request_token(self) -> CreateOAuthTokenResponse:
        attempt = 0
        while True:
            try:
                return await self._auth_client.create(
                    client_id=self._client_id,
                    client_assertion_type=CLIENT_ASSERTION_TYPE,
                    client_assertion=self._signer.sign(),
                    request_options={"max_retries": 0},
                )
            except Exception as e:
                if attempt >= _MAX_RETRIES or not _is_retryable(e):
                    raise
                await asyncio.sleep(0.5 * 2**attempt)
                attempt += 1
