import base64
import typing
from collections.abc import AsyncIterator, Iterator
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.proxy_response import ProxyResponse
from .raw_client import AsyncRawProxyClient, RawProxyClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

_SyncResult = typing.Union[ProxyResponse, typing.Iterator[bytes], None]
_AsyncResult = typing.Union[ProxyResponse, typing.AsyncIterator[bytes], None]


def _add_params_to_url(url: str, params: typing.Dict[str, typing.Any]) -> str:
    parsed = urlparse(url)
    existing_params = parse_qs(parsed.query)
    for key, value in params.items():
        existing_params[key] = value if isinstance(value, list) else [value]
    new_query = urlencode(existing_params, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


def _prepare_request(
    url: str,
    *,
    headers: typing.Optional[typing.Dict[str, typing.Any]],
    params: typing.Optional[typing.Dict[str, typing.Any]],
) -> typing.Tuple[str, RequestOptions]:
    if params:
        url = _add_params_to_url(url, params)
    url_64 = base64.urlsafe_b64encode(url.encode()).decode()
    downstream_headers = {
        f"x-pd-proxy-{name}": value for name, value in (headers or {}).items()
    }
    return url_64, RequestOptions(additional_headers=downstream_headers)


def _consume_sync(ctx: typing.ContextManager) -> _SyncResult:
    """
    Open the raw proxy context, peek at the response payload, and either
    return the parsed ProxyResponse (fully-buffered JSON) or a generator that
    streams the binary body and closes the underlying response when exhausted.
    """
    raw = ctx.__enter__()
    data = raw.data
    if not isinstance(data, Iterator):
        ctx.__exit__(None, None, None)
        return data

    def _stream() -> typing.Iterator[bytes]:
        try:
            yield from data
        finally:
            ctx.__exit__(None, None, None)

    return _stream()


async def _consume_async(ctx: typing.AsyncContextManager) -> _AsyncResult:
    """
    Async counterpart of `_consume_sync` — returns either a parsed
    ProxyResponse or an async generator that streams the binary body.
    """
    raw = await ctx.__aenter__()
    data = raw.data
    if not isinstance(data, AsyncIterator):
        await ctx.__aexit__(None, None, None)
        return data

    async def _stream() -> typing.AsyncIterator[bytes]:
        try:
            async for chunk in data:
                yield chunk
        finally:
            await ctx.__aexit__(None, None, None)

    return _stream()


class ProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProxyClient
        """
        return self._raw_client

    def get(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _SyncResult:
        """
        Forward an authenticated GET request to an external API using an external user's account credentials.

        Parameters
        ----------
        url : str
            Target URL

        external_user_id : str
            The external user ID for the proxy request

        account_id : str
            The account ID to use for authentication

        headers : typing.Optional[typing.Dict[str, typing.Any]]
            Additional headers to include in the request

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Query parameters to include in the request

        Returns
        -------
        typing.Union[ProxyResponse, typing.Iterator[bytes], None]
            ProxyResponse for JSON content, Iterator[bytes] for binary content, None for empty bodies.

        Examples
        --------
        from pipedream import Pipedream, PipedreamEnvironment

        client = Pipedream(
            client_id="<clientId>",
            client_secret="<clientSecret>",
            environment=PipedreamEnvironment.PROD,
        )
        client.proxy.get(
            url="https://example.com/api/endpoint",
            external_user_id="external_user_id",
            account_id="account_id",
            headers={"Extra-Downstream-Header": "some value"},
            params={"limit": 10},
        )
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return _consume_sync(
            self._raw_client.get(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request_options=request_options,
            )
        )

    def post(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _SyncResult:
        """
        Forward an authenticated POST request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return _consume_sync(
            self._raw_client.post(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request=body or {},
                request_options=request_options,
            )
        )

    def put(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _SyncResult:
        """
        Forward an authenticated PUT request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return _consume_sync(
            self._raw_client.put(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request=body or {},
                request_options=request_options,
            )
        )

    def patch(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _SyncResult:
        """
        Forward an authenticated PATCH request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return _consume_sync(
            self._raw_client.patch(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request=body or {},
                request_options=request_options,
            )
        )

    def delete(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _SyncResult:
        """
        Forward an authenticated DELETE request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return _consume_sync(
            self._raw_client.delete(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request_options=request_options,
            )
        )


class AsyncProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProxyClient
        """
        return self._raw_client

    async def get(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _AsyncResult:
        """
        Forward an authenticated GET request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return await _consume_async(
            self._raw_client.get(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request_options=request_options,
            )
        )

    async def post(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _AsyncResult:
        """
        Forward an authenticated POST request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return await _consume_async(
            self._raw_client.post(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request=body or {},
                request_options=request_options,
            )
        )

    async def put(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _AsyncResult:
        """
        Forward an authenticated PUT request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return await _consume_async(
            self._raw_client.put(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request=body or {},
                request_options=request_options,
            )
        )

    async def patch(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _AsyncResult:
        """
        Forward an authenticated PATCH request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return await _consume_async(
            self._raw_client.patch(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request=body or {},
                request_options=request_options,
            )
        )

    async def delete(
        self,
        url: str,
        *,
        external_user_id: str,
        account_id: str,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> _AsyncResult:
        """
        Forward an authenticated DELETE request to an external API using an external user's account credentials.
        """
        url_64, request_options = _prepare_request(url, headers=headers, params=params)
        return await _consume_async(
            self._raw_client.delete(
                url_64,
                external_user_id=external_user_id,
                account_id=account_id,
                request_options=request_options,
            )
        )
