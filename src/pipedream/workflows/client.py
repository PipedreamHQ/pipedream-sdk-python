import enum
import re
import typing

import httpx

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

_DEFAULT_WORKFLOW_DOMAIN = "m.pipedream.net"
_ENDPOINT_ID_RE = re.compile(r"^e(n|o)[a-z0-9-]+$")


class HTTPAuthType(enum.Enum):
    """Authentication types for workflow invocation."""

    NONE = "none"
    STATIC_BEARER = "static_bearer_token"
    OAUTH = "oauth"


def _is_endpoint_id(url_or_endpoint: str) -> bool:
    return bool(_ENDPOINT_ID_RE.match(url_or_endpoint))


def _build_workflow_url(url_or_endpoint: str, *, workflow_domain: str) -> str:
    if not url_or_endpoint:
        raise ValueError("URL or endpoint ID is required")

    if url_or_endpoint.startswith(("http://", "https://")):
        return url_or_endpoint

    if "." in url_or_endpoint and not _is_endpoint_id(url_or_endpoint):
        return f"https://{url_or_endpoint}"

    if not _is_endpoint_id(url_or_endpoint):
        raise ValueError(f"Invalid endpoint ID format: {url_or_endpoint}")

    return f"https://{url_or_endpoint}.{workflow_domain}"


def _prepare_headers(
    headers: typing.Optional[typing.Dict[str, str]],
    auth_type: HTTPAuthType,
) -> typing.Dict[str, str]:
    request_headers = dict(headers) if headers else {}
    if auth_type == HTTPAuthType.NONE:
        # Suppress the default bearer token added by the client wrapper.
        request_headers["Authorization"] = ""
    return request_headers


def _add_external_user_id_header(
    headers: typing.Optional[typing.Dict[str, str]],
    external_user_id: str,
) -> typing.Dict[str, str]:
    if not external_user_id:
        raise ValueError("external_user_id is required")
    request_headers = dict(headers) if headers else {}
    request_headers["X-PD-External-User-ID"] = external_user_id
    return request_headers


class WorkflowsClient:
    def __init__(
        self,
        *,
        client_wrapper: SyncClientWrapper,
        workflow_domain: str = _DEFAULT_WORKFLOW_DOMAIN,
    ):
        self._client_wrapper = client_wrapper
        self._workflow_domain = workflow_domain

    def invoke(
        self,
        url_or_endpoint: str,
        *,
        method: str = "POST",
        body: typing.Optional[typing.Any] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        auth_type: HTTPAuthType = HTTPAuthType.NONE,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Invoke a workflow via its HTTP interface URL or endpoint ID.

        Parameters
        ----------
        url_or_endpoint : str
            The full URL of the workflow's HTTP interface or the endpoint ID.

        method : str
            HTTP method to use (default: "POST").

        body : typing.Optional[typing.Any]
            Request body. Dict/list values are serialized as JSON; other types are sent as raw form data.

        headers : typing.Optional[typing.Dict[str, str]]
            Additional HTTP headers to include.

        auth_type : HTTPAuthType
            Authentication mode (default: HTTPAuthType.NONE).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        httpx.Response
            Response returned by the invoked workflow.

        Examples
        --------
        from pipedream import Pipedream, PipedreamEnvironment
        from pipedream.workflows.client import HTTPAuthType

        client = Pipedream(
            client_id="<clientId>",
            client_secret="<clientSecret>",
            environment=PipedreamEnvironment.PROD,
        )
        response = client.workflows.invoke(
            url_or_endpoint="https://your-workflow.m.pipedream.net",
            method="POST",
            body={"key": "value"},
            headers={"Content-Type": "application/json"},
            auth_type=HTTPAuthType.NONE,
        )
        """
        workflow_url = _build_workflow_url(url_or_endpoint, workflow_domain=self._workflow_domain)
        request_headers = _prepare_headers(headers, auth_type)

        response = self._client_wrapper.httpx_client.request(
            workflow_url,
            method=method,
            data=body,
            json=body,
            headers=request_headers,
            request_options=request_options,
        )
        response.raise_for_status()
        return response

    def invoke_for_external_user(
        self,
        url_or_endpoint: str,
        *,
        external_user_id: str,
        method: str = "POST",
        body: typing.Optional[typing.Any] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Invoke a workflow on behalf of a Pipedream Connect end-user.

        Forces OAuth authentication and adds the `X-PD-External-User-ID` header.

        Parameters
        ----------
        url_or_endpoint : str
            The full URL of the workflow's HTTP interface or the endpoint ID.

        external_user_id : str
            The external user ID for whom the workflow is being invoked.

        method : str
            HTTP method to use (default: "POST").

        body : typing.Optional[typing.Any]
            Request body. Dict/list values are serialized as JSON; other types are sent as raw form data.

        headers : typing.Optional[typing.Dict[str, str]]
            Additional HTTP headers to include.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        httpx.Response
            Response returned by the invoked workflow.

        Examples
        --------
        from pipedream import Pipedream, PipedreamEnvironment

        client = Pipedream(
            client_id="<clientId>",
            client_secret="<clientSecret>",
            environment=PipedreamEnvironment.PROD,
        )
        response = client.workflows.invoke_for_external_user(
            url_or_endpoint="en2r1n8a98np7",
            external_user_id="user_123",
            method="POST",
            body={"message": "Hello from external user"},
            headers={"Content-Type": "application/json"},
        )
        """
        return self.invoke(
            url_or_endpoint,
            method=method,
            body=body,
            headers=_add_external_user_id_header(headers, external_user_id),
            auth_type=HTTPAuthType.OAUTH,
            request_options=request_options,
        )


class AsyncWorkflowsClient:
    def __init__(
        self,
        *,
        client_wrapper: AsyncClientWrapper,
        workflow_domain: str = _DEFAULT_WORKFLOW_DOMAIN,
    ):
        self._client_wrapper = client_wrapper
        self._workflow_domain = workflow_domain

    async def invoke(
        self,
        url_or_endpoint: str,
        *,
        method: str = "POST",
        body: typing.Optional[typing.Any] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        auth_type: HTTPAuthType = HTTPAuthType.NONE,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Async counterpart of `WorkflowsClient.invoke`.
        """
        workflow_url = _build_workflow_url(url_or_endpoint, workflow_domain=self._workflow_domain)
        request_headers = _prepare_headers(headers, auth_type)

        response = await self._client_wrapper.httpx_client.request(
            workflow_url,
            method=method,
            data=body,
            json=body,
            headers=request_headers,
            request_options=request_options,
        )
        response.raise_for_status()
        return response

    async def invoke_for_external_user(
        self,
        url_or_endpoint: str,
        *,
        external_user_id: str,
        method: str = "POST",
        body: typing.Optional[typing.Any] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Async counterpart of `WorkflowsClient.invoke_for_external_user`.
        """
        return await self.invoke(
            url_or_endpoint,
            method=method,
            body=body,
            headers=_add_external_user_id_header(headers, external_user_id),
            auth_type=HTTPAuthType.OAUTH,
            request_options=request_options,
        )
