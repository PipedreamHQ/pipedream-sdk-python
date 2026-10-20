import os
import typing

import httpx
from .client import AsyncClient, Client
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .private_key_jwt import (
    AsyncPrivateKeyJwtTokenProvider,
    ClientAssertionSigner,
    PrivateKeyJwtTokenProvider,
    issuer_from_base_url,
)
from .types.project_environment import ProjectEnvironment
from .workflows.client import AsyncWorkflowsClient, WorkflowsClient

_PROD_BASE_URL = "https://api.pipedream.com"


def normalize_url_path(request: httpx.Request) -> None:
    request.url = request.url.copy_with(
        path=request.url.path.replace("//", "/"),
    )


async def async_normalize_url_path(request: httpx.Request) -> None:
    normalize_url_path(request)


def install_request_hook(
    client_wrapper: SyncClientWrapper | AsyncClientWrapper,
    hook: typing.Callable,
) -> None:
    client_wrapper.httpx_client.httpx_client.event_hooks.setdefault(
        "request",
        [],
    ).append(hook)


def _resolve_credentials(
    client_secret: typing.Optional[str],
    private_key: typing.Optional[str],
) -> typing.Tuple[typing.Optional[str], typing.Optional[str]]:
    """Returns (client_secret, private_key) with at most one of them set.

    An explicitly passed credential wins over the other one in the environment.
    Passing both, or setting both PIPEDREAM_CLIENT_SECRET and
    PIPEDREAM_PRIVATE_KEY with neither passed, raises ValueError.
    """
    env_secret = os.getenv("PIPEDREAM_CLIENT_SECRET")
    # client_secret defaults to the environment variable, so a value equal to
    # it is treated as coming from the environment.
    secret_passed = bool(client_secret) and client_secret != env_secret
    if private_key and secret_passed:
        raise ValueError("Pass either client_secret or private_key, not both")
    if private_key:
        return None, private_key
    if secret_passed:
        return client_secret, None
    env_key = os.getenv("PIPEDREAM_PRIVATE_KEY")
    if client_secret and env_key:
        raise ValueError(
            "Both PIPEDREAM_CLIENT_SECRET and PIPEDREAM_PRIVATE_KEY are set; set only the one your client uses"
        )
    return client_secret, env_key


def _assertion_signer(
    client_id: typing.Optional[str],
    private_key: str,
    key_id: typing.Optional[str],
    base_url: str,
) -> ClientAssertionSigner:
    if not client_id:
        raise ValueError("client_id is required when authenticating with private_key")
    return ClientAssertionSigner(
        client_id=client_id,
        private_key=private_key,
        key_id=key_id or os.getenv("PIPEDREAM_KEY_ID"),
        # The assertion audience is the API's issuer identifier: the base URL's
        # origin (https://api.pipedream.com by default).
        audience=issuer_from_base_url(base_url),
    )


class Pipedream(Client):

    def __init__(
        self,
        *,
        access_token: typing.Optional[str] = os.getenv("PIPEDREAM_ACCESS_TOKEN"),
        client_id: typing.Optional[str] = os.getenv("PIPEDREAM_CLIENT_ID"),
        client_secret: typing.Optional[str] = os.getenv("PIPEDREAM_CLIENT_SECRET"),
        private_key: typing.Optional[str] = None,
        key_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = os.getenv("PIPEDREAM_PROJECT_ID"),
        project_environment: typing.Optional[ProjectEnvironment] = os.getenv(
            "PIPEDREAM_PROJECT_ENVIRONMENT",
            "production",
        ),
        base_url: typing.Optional[str] = None,
        workflow_domain: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        # Ensure that project IDs are strings
        project_id = project_id or ""

        resolved_base_url = base_url or os.environ.get("PIPEDREAM_BASE_URL") or _PROD_BASE_URL
        resolved_workflow_domain = (
            workflow_domain or os.environ.get("PIPEDREAM_WORKFLOW_DOMAIN") or "m.pipedream.net"
        )

        common_kwargs: typing.Dict[str, typing.Any] = dict(
            base_url=resolved_base_url,
            project_id=project_id,
            project_environment=project_environment,
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )

        client_secret, private_key = _resolve_credentials(client_secret, private_key)

        if access_token:
            super().__init__(token=(lambda: access_token), **common_kwargs)
        elif private_key:
            signer = _assertion_signer(client_id, private_key, key_id, resolved_base_url)
            super().__init__(token=lambda: self._token_provider.get_token(), **common_kwargs)
            # Token requests use their own unauthenticated wrapper over the same
            # HTTP client, like the generated client-secret flow.
            wrapper = self._client_wrapper
            self._token_provider = PrivateKeyJwtTokenProvider(
                client_id=typing.cast(str, client_id),
                signer=signer,
                client_wrapper=SyncClientWrapper(
                    project_id=project_id,
                    project_environment=project_environment,
                    headers=headers,
                    base_url=wrapper.get_base_url(),
                    timeout=wrapper.get_timeout(),
                    max_retries=wrapper.get_max_retries(),
                    logging=logging,
                    httpx_client=wrapper.httpx_client.httpx_client,
                ),
            )
        else:
            super().__init__(client_id=client_id, client_secret=client_secret, **common_kwargs)

        install_request_hook(self._client_wrapper, normalize_url_path)

        self.workflows = WorkflowsClient(
            client_wrapper=self._client_wrapper,
            workflow_domain=resolved_workflow_domain,
        )

    @property
    def raw_access_token(self) -> typing.Optional[str]:
        """
        Returns an access token that can be used to authenticate API requests
        """
        return self._client_wrapper._get_token()


class AsyncPipedream(AsyncClient):

    def __init__(
        self,
        *,
        access_token: typing.Optional[str] = os.getenv("PIPEDREAM_ACCESS_TOKEN"),
        client_id: typing.Optional[str] = os.getenv("PIPEDREAM_CLIENT_ID"),
        client_secret: typing.Optional[str] = os.getenv("PIPEDREAM_CLIENT_SECRET"),
        private_key: typing.Optional[str] = None,
        key_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = os.getenv("PIPEDREAM_PROJECT_ID"),
        project_environment: typing.Optional[ProjectEnvironment] = os.getenv(
            "PIPEDREAM_PROJECT_ENVIRONMENT",
            "production",
        ),
        base_url: typing.Optional[str] = None,
        workflow_domain: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        # Ensure that project IDs are strings
        project_id = project_id or ""

        resolved_base_url = base_url or os.environ.get("PIPEDREAM_BASE_URL") or _PROD_BASE_URL
        resolved_workflow_domain = (
            workflow_domain or os.environ.get("PIPEDREAM_WORKFLOW_DOMAIN") or "m.pipedream.net"
        )

        common_kwargs: typing.Dict[str, typing.Any] = dict(
            base_url=resolved_base_url,
            project_id=project_id,
            project_environment=project_environment,
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )

        client_secret, private_key = _resolve_credentials(client_secret, private_key)

        if access_token:
            super().__init__(token=(lambda: access_token), **common_kwargs)
        elif private_key:
            signer = _assertion_signer(client_id, private_key, key_id, resolved_base_url)
            super().__init__(token=(lambda: ""), **common_kwargs)
            # Wire the async token provider the way the generated client-secret
            # flow does: no sync token, an async one, and token requests on
            # their own unauthenticated wrapper over the same HTTP client.
            wrapper = self._client_wrapper
            token_provider = AsyncPrivateKeyJwtTokenProvider(
                client_id=typing.cast(str, client_id),
                signer=signer,
                client_wrapper=AsyncClientWrapper(
                    project_id=project_id,
                    project_environment=project_environment,
                    headers=headers,
                    base_url=wrapper.get_base_url(),
                    timeout=wrapper.get_timeout(),
                    max_retries=wrapper.get_max_retries(),
                    logging=logging,
                    httpx_client=wrapper.httpx_client.httpx_client,
                ),
            )
            wrapper._token = None
            wrapper._async_token = token_provider.get_token
        else:
            super().__init__(client_id=client_id, client_secret=client_secret, **common_kwargs)

        install_request_hook(self._client_wrapper, async_normalize_url_path)

        self.workflows = AsyncWorkflowsClient(
            client_wrapper=self._client_wrapper,
            workflow_domain=resolved_workflow_domain,
        )

    @property
    def raw_access_token(self) -> typing.Optional[str]:
        """
        Returns an access token that can be used to authenticate API requests
        """
        return self._client_wrapper._get_token()
