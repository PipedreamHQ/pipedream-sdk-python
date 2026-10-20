"""Private key (private_key_jwt) client authentication: the SDK signs a client
assertion for each token request instead of sending a client secret."""

import json
import typing

import httpx
import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, rsa

from pipedream import AsyncPipedream, Pipedream
from pipedream.private_key_jwt import ClientAssertionSigner

ASSERTION_TYPE = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
_ACCOUNTS_BODY: dict = {"data": [], "page_info": {}}


def _pem(key: typing.Any) -> str:
    return key.private_bytes(
        serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()
    ).decode()


def _ec_key() -> ec.EllipticCurvePrivateKey:
    return ec.generate_private_key(ec.SECP256R1())


def _decode(assertion: str, public_key: typing.Any, audience: str) -> typing.Dict[str, typing.Any]:
    return jwt.decode(assertion, public_key, algorithms=["ES256", "RS256"], audience=audience)


class TestClientAssertionSigner:
    def test_signs_es256_with_client_claims_and_a_fresh_jti(self) -> None:
        # Arrange
        key = _ec_key()
        signer = ClientAssertionSigner(
            client_id="client_123", private_key=_pem(key), audience="https://api.pipedream.com"
        )

        # Act
        first, second = signer.sign(), signer.sign()

        # Assert
        assert jwt.get_unverified_header(first) == {"alg": "ES256", "typ": "client-authentication+jwt"}
        claims = _decode(first, key.public_key(), "https://api.pipedream.com")
        assert claims["iss"] == claims["sub"] == "client_123"
        assert claims["exp"] - claims["iat"] == 60
        assert _decode(second, key.public_key(), "https://api.pipedream.com")["jti"] != claims["jti"]

    def test_signs_rs256_with_an_rsa_key_and_sends_key_id(self) -> None:
        # Arrange
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        signer = ClientAssertionSigner(
            client_id="c", private_key=_pem(key), key_id="key-2026", audience="https://api.pipedream.com"
        )

        # Act
        assertion = signer.sign()

        # Assert
        assert jwt.get_unverified_header(assertion)["alg"] == "RS256"
        assert jwt.get_unverified_header(assertion)["kid"] == "key-2026"
        _decode(assertion, key.public_key(), "https://api.pipedream.com")

    def test_accepts_a_jwk_private_key_and_uses_its_kid(self) -> None:
        # Arrange
        key = _ec_key()
        jwk = json.loads(jwt.algorithms.ECAlgorithm.to_jwk(key))
        jwk["kid"] = "jwk-kid"
        signer = ClientAssertionSigner(client_id="c", private_key=json.dumps(jwk), audience="https://api.pipedream.com")

        # Act
        assertion = signer.sign()

        # Assert
        assert jwt.get_unverified_header(assertion)["kid"] == "jwk-kid"
        _decode(assertion, key.public_key(), "https://api.pipedream.com")

    @pytest.mark.parametrize(
        "make_key",
        [
            lambda: _ec_key()
            .public_key()
            .public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
            .decode(),
            lambda: _pem(ec.generate_private_key(ec.SECP384R1())),
            lambda: _pem(ed25519.Ed25519PrivateKey.generate()),
            lambda: "not a key",
        ],
        ids=["public key", "P-384 key", "Ed25519 key", "garbage"],
    )
    def test_rejects_unusable_keys(self, make_key: typing.Callable[[], str]) -> None:
        # Act / Assert
        with pytest.raises(ValueError, match="private_key must be"):
            ClientAssertionSigner(client_id="c", private_key=make_key(), audience="https://api.pipedream.com")

    def test_explains_how_to_install_the_extra_when_pyjwt_is_missing(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # Arrange
        monkeypatch.setitem(__import__("sys").modules, "jwt", None)

        # Act / Assert
        with pytest.raises(ImportError, match=r"pipedream\[private-key\]"):
            ClientAssertionSigner(client_id="c", private_key=_pem(_ec_key()), audience="https://api.pipedream.com")


class _TokenEndpoint:
    """An httpx handler for the token endpoint (answering with the given statuses
    in order, the last one repeating) and a Connect accounts endpoint."""

    def __init__(self, statuses: typing.Sequence[int] = (200,)):
        self.statuses = list(statuses)
        self.token_requests: typing.List[typing.Dict[str, typing.Any]] = []
        self.api_auth_headers: typing.List[typing.Optional[str]] = []

    def respond(self, request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/oauth/token":
            self.token_requests.append(json.loads(request.content))
            n = len(self.token_requests)
            status = self.statuses[min(n - 1, len(self.statuses) - 1)]
            if status == 200:
                return httpx.Response(
                    200, json={"access_token": f"token-{n}", "token_type": "bearer", "expires_in": 3600}
                )
            return httpx.Response(
                status, json={"error": "invalid_client" if status == 401 else "temporarily_unavailable"}
            )
        self.api_auth_headers.append(request.headers.get("authorization"))
        return httpx.Response(200, json=_ACCOUNTS_BODY)


def _client(endpoint: _TokenEndpoint, key: typing.Any) -> Pipedream:
    return Pipedream(
        client_id="client_123",
        private_key=_pem(key),
        key_id="kid-1",
        project_id="proj_123",
        base_url="https://api.example.com/",
        httpx_client=httpx.Client(transport=httpx.MockTransport(endpoint.respond)),
    )


class TestSyncClient:
    def test_authenticates_with_a_client_assertion_and_caches_the_token(self) -> None:
        # Arrange
        key = _ec_key()
        endpoint = _TokenEndpoint()
        client = _client(endpoint, key)

        # Act
        client.accounts.list()
        client.accounts.list()

        # Assert
        assert endpoint.api_auth_headers == ["Bearer token-1", "Bearer token-1"]
        assert len(endpoint.token_requests) == 1
        body = endpoint.token_requests[0]
        assertion = body.pop("client_assertion")
        assert body == {
            "grant_type": "client_credentials",
            "client_id": "client_123",
            "client_assertion_type": ASSERTION_TYPE,
        }
        assert jwt.get_unverified_header(assertion)["kid"] == "kid-1"
        # The audience is the API's issuer: the base URL's origin.
        claims = _decode(assertion, key.public_key(), "https://api.example.com")
        assert claims["iss"] == claims["sub"] == "client_123"
        assert client.raw_access_token == "token-1"

    def test_retries_a_transient_failure_with_a_newly_signed_assertion(self) -> None:
        # Arrange
        endpoint = _TokenEndpoint(statuses=[503, 200])
        client = _client(endpoint, _ec_key())

        # Act
        token = client.raw_access_token

        # Assert
        assert token == "token-2"
        jtis = [
            jwt.decode(r["client_assertion"], options={"verify_signature": False})["jti"]
            for r in endpoint.token_requests
        ]
        assert len(jtis) == 2 and jtis[0] != jtis[1]

    def test_does_not_retry_a_rejected_assertion(self) -> None:
        # Arrange
        endpoint = _TokenEndpoint(statuses=[401])
        client = _client(endpoint, _ec_key())

        # Act / Assert
        with pytest.raises(Exception):
            client.accounts.list()
        assert len(endpoint.token_requests) == 1


async def test_async_client_authenticates_with_a_client_assertion() -> None:
    # Arrange
    endpoint = _TokenEndpoint()

    async def handler(request: httpx.Request) -> httpx.Response:
        return endpoint.respond(request)

    client = AsyncPipedream(
        client_id="client_123",
        private_key=_pem(_ec_key()),
        project_id="proj_123",
        base_url="https://api.example.com",
        httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
    )

    # Act
    await client.accounts.list()
    await client.accounts.list()

    # Assert
    assert endpoint.api_auth_headers == ["Bearer token-1", "Bearer token-1"]
    assert len(endpoint.token_requests) == 1
    assert "client_secret" not in endpoint.token_requests[0]
    assert endpoint.token_requests[0]["client_assertion_type"] == ASSERTION_TYPE


class TestCredentialResolution:
    @pytest.fixture(autouse=True)
    def _clean_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        for name in ("PIPEDREAM_CLIENT_SECRET", "PIPEDREAM_PRIVATE_KEY", "PIPEDREAM_KEY_ID", "PIPEDREAM_ACCESS_TOKEN"):
            monkeypatch.delenv(name, raising=False)

    def test_refuses_a_client_secret_and_a_private_key_together(self) -> None:
        # Act / Assert
        with pytest.raises(ValueError, match="not both"):
            Pipedream(client_id="c", client_secret="s", private_key=_pem(_ec_key()), project_id="p")

    def test_reads_pipedream_private_key_from_the_environment(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # Arrange
        monkeypatch.setenv("PIPEDREAM_PRIVATE_KEY", _pem(_ec_key()))

        # Act
        client = Pipedream(client_id="c", client_secret=None, project_id="p")

        # Assert
        assert hasattr(client, "_token_provider")

    def test_refuses_both_credentials_from_the_environment(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # Arrange: client_secret defaults to PIPEDREAM_CLIENT_SECRET.
        monkeypatch.setenv("PIPEDREAM_CLIENT_SECRET", "from-env")
        monkeypatch.setenv("PIPEDREAM_PRIVATE_KEY", _pem(_ec_key()))

        # Act / Assert
        with pytest.raises(ValueError, match="set only the one your client uses"):
            Pipedream(client_id="c", client_secret="from-env", project_id="p")

    def test_an_explicit_private_key_overrides_a_secret_in_the_environment(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # Arrange
        monkeypatch.setenv("PIPEDREAM_CLIENT_SECRET", "from-env")

        # Act
        client = Pipedream(client_id="c", client_secret="from-env", private_key=_pem(_ec_key()), project_id="p")

        # Assert
        assert hasattr(client, "_token_provider")

    def test_requires_a_client_id_with_a_private_key(self) -> None:
        # Act / Assert
        with pytest.raises(ValueError, match="client_id is required"):
            Pipedream(client_id=None, client_secret=None, private_key=_pem(_ec_key()), project_id="p")

    def test_client_secret_auth_is_unchanged(self) -> None:
        # Act
        client = Pipedream(client_id="c", client_secret="s", project_id="p")

        # Assert
        assert not hasattr(client, "_token_provider")
