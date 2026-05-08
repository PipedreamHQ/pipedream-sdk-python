import contextlib
import typing
from json.decoder import JSONDecodeError

from pydantic import ValidationError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.proxy_response import ProxyResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

_ProxyData = typing.Optional[typing.Union[ProxyResponse, typing.Iterator[bytes]]]
_AsyncProxyData = typing.Optional[typing.Union[ProxyResponse, typing.AsyncIterator[bytes]]]


def _is_json_content_type(content_type: str) -> bool:
    return "application/json" in content_type or not content_type


def _decode_error_body(_response: typing.Any) -> typing.Any:
    error_content_type = _response.headers.get("content-type", "").lower()
    if "application/json" in error_content_type:
        return _response.json()
    return _response.text


class RawProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def get(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[_ProxyData]]:
        """
        Forward an authenticated GET request to an external API using an external user's account credentials.

        Parameters
        ----------
        url_64 : str
            Base64-encoded target URL

        external_user_id : str
            The external user ID for the proxy request

        account_id : str
            The account ID to use for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Optional[typing.Union[ProxyResponse, typing.Iterator[bytes]]]]]
            proxy request successful
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="GET",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            request_options=request_options,
        ) as _response:
            yield _handle_sync_response(_response, request_options)

    @contextlib.contextmanager
    def post(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[_ProxyData]]:
        """
        Forward an authenticated POST request to an external API using an external user's account credentials.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="POST",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            json=request,
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            yield _handle_sync_response(_response, request_options)

    @contextlib.contextmanager
    def put(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[_ProxyData]]:
        """
        Forward an authenticated PUT request to an external API using an external user's account credentials.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="PUT",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            json=request,
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            yield _handle_sync_response(_response, request_options)

    @contextlib.contextmanager
    def patch(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[_ProxyData]]:
        """
        Forward an authenticated PATCH request to an external API using an external user's account credentials.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="PATCH",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            json=request,
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            yield _handle_sync_response(_response, request_options)

    @contextlib.contextmanager
    def delete(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[_ProxyData]]:
        """
        Forward an authenticated DELETE request to an external API using an external user's account credentials.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="DELETE",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            request_options=request_options,
        ) as _response:
            yield _handle_sync_response(_response, request_options)


class AsyncRawProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def get(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[_AsyncProxyData]]:
        """
        Forward an authenticated GET request to an external API using an external user's account credentials.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="GET",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            request_options=request_options,
        ) as _response:
            yield await _handle_async_response(_response, request_options)

    @contextlib.asynccontextmanager
    async def post(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[_AsyncProxyData]]:
        """
        Forward an authenticated POST request to an external API using an external user's account credentials.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="POST",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            json=request,
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            yield await _handle_async_response(_response, request_options)

    @contextlib.asynccontextmanager
    async def put(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[_AsyncProxyData]]:
        """
        Forward an authenticated PUT request to an external API using an external user's account credentials.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="PUT",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            json=request,
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            yield await _handle_async_response(_response, request_options)

    @contextlib.asynccontextmanager
    async def patch(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[_AsyncProxyData]]:
        """
        Forward an authenticated PATCH request to an external API using an external user's account credentials.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="PATCH",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            json=request,
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            yield await _handle_async_response(_response, request_options)

    @contextlib.asynccontextmanager
    async def delete(
        self,
        url_64: str,
        *,
        external_user_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[_AsyncProxyData]]:
        """
        Forward an authenticated DELETE request to an external API using an external user's account credentials.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/connect/{encode_path_param(self._client_wrapper._project_id)}/proxy/{encode_path_param(url_64)}",
            method="DELETE",
            params={
                "external_user_id": external_user_id,
                "account_id": account_id,
            },
            request_options=request_options,
        ) as _response:
            yield await _handle_async_response(_response, request_options)


def _handle_sync_response(
    _response: typing.Any, request_options: typing.Optional[RequestOptions]
) -> HttpResponse[_ProxyData]:
    try:
        if 200 <= _response.status_code < 300:
            content_type = _response.headers.get("content-type", "").lower()
            if _is_json_content_type(content_type):
                _response.read()
                if not _response.text.strip():
                    return HttpResponse(response=_response, data=None)
                _data = typing.cast(
                    ProxyResponse,
                    parse_obj_as(
                        type_=ProxyResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
            return HttpResponse(
                response=_response,
                data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size)),
            )
        _response.read()
        if _response.status_code == 429:
            raise TooManyRequestsError(
                headers=dict(_response.headers),
                body=typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_decode_error_body(_response),
                    ),
                ),
            )
        _response_body = _decode_error_body(_response)
    except JSONDecodeError:
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response.text,
        )
    except ValidationError as e:
        raise ParsingError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response.json(),
            cause=e,
        )
    raise ApiError(
        status_code=_response.status_code,
        headers=dict(_response.headers),
        body=_response_body,
    )


async def _handle_async_response(
    _response: typing.Any, request_options: typing.Optional[RequestOptions]
) -> AsyncHttpResponse[_AsyncProxyData]:
    try:
        if 200 <= _response.status_code < 300:
            content_type = _response.headers.get("content-type", "").lower()
            if _is_json_content_type(content_type):
                await _response.aread()
                if not _response.text.strip():
                    return AsyncHttpResponse(response=_response, data=None)
                _data = typing.cast(
                    ProxyResponse,
                    parse_obj_as(
                        type_=ProxyResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
            return AsyncHttpResponse(
                response=_response,
                data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
            )
        await _response.aread()
        if _response.status_code == 429:
            raise TooManyRequestsError(
                headers=dict(_response.headers),
                body=typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_decode_error_body(_response),
                    ),
                ),
            )
        _response_body = _decode_error_body(_response)
    except JSONDecodeError:
        raise ApiError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response.text,
        )
    except ValidationError as e:
        raise ParsingError(
            status_code=_response.status_code,
            headers=dict(_response.headers),
            body=_response.json(),
            cause=e,
        )
    raise ApiError(
        status_code=_response.status_code,
        headers=dict(_response.headers),
        body=_response_body,
    )
