import os
import typing

import httpx

from .client import AsyncClient, Client
from .core.logging import LogConfig, Logger
from .types.project_environment import ProjectEnvironment
from .workflows.client import AsyncWorkflowsClient, WorkflowsClient

_PROD_BASE_URL = "https://api.pipedream.com"


class Pipedream(Client):

    def __init__(
        self,
        *,
        access_token: typing.Optional[str] = os.getenv("PIPEDREAM_ACCESS_TOKEN"),
        client_id: typing.Optional[str] = os.getenv("PIPEDREAM_CLIENT_ID"),
        client_secret: typing.Optional[str] = os.getenv("PIPEDREAM_CLIENT_SECRET"),
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
        if not project_id:
            raise ValueError("Project ID is required")

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

        if access_token:
            super().__init__(token=(lambda: access_token), **common_kwargs)
        else:
            super().__init__(client_id=client_id, client_secret=client_secret, **common_kwargs)

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
        if not project_id:
            raise ValueError("Project ID is required")

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

        if access_token:
            super().__init__(token=(lambda: access_token), **common_kwargs)
        else:
            super().__init__(client_id=client_id, client_secret=client_secret, **common_kwargs)

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
