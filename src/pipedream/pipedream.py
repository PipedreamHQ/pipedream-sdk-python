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
        timeout: Optional[float] = None,
    ):
        if not project_id:
            raise ValueError("Project ID is required")

        if access_token:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                token=(lambda: access_token),
                timeout=timeout,
            )
        else:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                client_id=client_id,
                client_secret=client_secret,
                timeout=timeout,
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
        timeout: Optional[float] = None,
    ):
        if not project_id:
            raise ValueError("Project ID is required")

        if access_token:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                token=(lambda: access_token),
                timeout=timeout,
            )
        else:
            super().__init__(
                base_url=_get_base_url(environment),
                project_environment=project_environment,
                project_id=project_id,
                client_id=client_id,
                client_secret=client_secret,
                timeout=timeout,
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
        Returns an access token that can be used to authenticate API requests
        """
        return self._client_wrapper._get_token()


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
