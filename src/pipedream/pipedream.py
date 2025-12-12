import os
from typing import Optional

from .client import (
    AsyncClient,
    Client,
)
from .environment import PipedreamEnvironment
from .types.project_environment import ProjectEnvironment
from .workflows.client import (
    AsyncWorkflowsClient,
    WorkflowsClient,
)


class Pipedream(Client):

    def __init__(
        self,
        *,
        access_token: Optional[str] = os.getenv("PIPEDREAM_ACCESS_TOKEN"),
        client_id: Optional[str] = os.getenv("PIPEDREAM_CLIENT_ID"),
        client_secret: Optional[str] = os.getenv("PIPEDREAM_CLIENT_SECRET"),
        project_id: Optional[str] = os.getenv("PIPEDREAM_PROJECT_ID"),
        project_environment: ProjectEnvironment = os.getenv(
            "PIPEDREAM_PROJECT_ENVIRONMENT",
            "production",
        ),
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
        workflow_domain: Optional[str] = None,
    ):
        if not project_id:
            raise ValueError("Project ID is required")

        if access_token:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                token=(lambda: access_token),
            )
        else:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                client_id=client_id,
                client_secret=client_secret,
            )

        if not workflow_domain:
            workflow_domain = _get_default_workflow_domain(environment)

        self.workflows = WorkflowsClient(
            client_wrapper=self._client_wrapper,
            workflow_domain=workflow_domain,
        )

    @property
    def raw_access_token(self) -> Optional[str]:
        """
        Returns an access token that can be used to authenticate API requests
        """
        return self._client_wrapper._get_token()


class AsyncPipedream(AsyncClient):

    def __init__(
        self,
        *,
        access_token: Optional[str] = os.getenv("PIPEDREAM_ACCESS_TOKEN"),
        client_id: Optional[str] = os.getenv("PIPEDREAM_CLIENT_ID"),
        client_secret: Optional[str] = os.getenv("PIPEDREAM_CLIENT_SECRET"),
        project_id: Optional[str] = os.getenv("PIPEDREAM_PROJECT_ID"),
        project_environment: ProjectEnvironment = os.getenv(
            "PIPEDREAM_PROJECT_ENVIRONMENT",
            "production",
        ),
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
        workflow_domain: Optional[str] = None,
    ):
        if not project_id:
            raise ValueError("Project ID is required")

        if access_token:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                token=(lambda: access_token),
            )
        else:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                client_id=client_id,
                client_secret=client_secret,
            )

        if not workflow_domain:
            workflow_domain = _get_default_workflow_domain(environment)

        self.workflows = AsyncWorkflowsClient(
            client_wrapper=self._client_wrapper,
            workflow_domain=workflow_domain,
        )

    @property
    def raw_access_token(self) -> Optional[str]:
        """
        Returns an access token that can be used to authenticate API requests.

        Note: When using OAuth authentication (`client_id`/`client_secret`),
        this property may perform blocking network operations. For async
        applications, prefer using the async property `async_raw_access_token`
        instead.
        """
        return self._client_wrapper._get_token()

    @property
    async def async_raw_access_token(self) -> Optional[str]:
        """
        Asynchronously returns an access token that can be used to authenticate
        API requests.

        This method is non-blocking and safe to use in async contexts such as
        FastAPI, Django ASGI, or any other asyncio-based application.
        """
        if self._client_wrapper._async_token is not None:
            return await self._client_wrapper._async_token()
        return self.raw_access_token


def _get_base_url(environment: PipedreamEnvironment) -> str:
    """
    Returns the base URL for the given environment.
    """
    return os.path.expandvars(environment.value)


def _get_default_workflow_domain(environment: PipedreamEnvironment) -> str:
    """
    Returns the default workflow domain.
    """
    if environment == PipedreamEnvironment.DEV:
        return "m.d.pipedream.net"
    return "m.pipedream.net"
