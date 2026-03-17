import os
from typing import Optional

from .client import (
    AsyncClient,
    Client,
)
from .types.project_environment import ProjectEnvironment
from .workflows.client import (
    AsyncWorkflowsClient,
    WorkflowsClient,
)

_PROD_BASE_URL = "https://api.pipedream.com"


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
        base_url: Optional[str] = None,
        workflow_domain: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        if not project_id:
            raise ValueError("Project ID is required")

        resolved_base_url = base_url or os.environ.get("PIPEDREAM_BASE_URL") or _PROD_BASE_URL
        resolved_workflow_domain = workflow_domain or os.environ.get("PIPEDREAM_WORKFLOW_DOMAIN") or "m.pipedream.net"

        if access_token:
            super().__init__(
                base_url=resolved_base_url,
                project_environment=project_environment,
                project_id=project_id,
                token=(lambda: access_token),
                timeout=timeout,
            )
        else:
            super().__init__(
                base_url=resolved_base_url,
                project_environment=project_environment,
                project_id=project_id,
                client_id=client_id,
                client_secret=client_secret,
                timeout=timeout,
            )

        self.workflows = WorkflowsClient(
            client_wrapper=self._client_wrapper,
            workflow_domain=resolved_workflow_domain,
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
        base_url: Optional[str] = None,
        workflow_domain: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        if not project_id:
            raise ValueError("Project ID is required")

        resolved_base_url = base_url or os.environ.get("PIPEDREAM_BASE_URL") or _PROD_BASE_URL
        resolved_workflow_domain = workflow_domain or os.environ.get("PIPEDREAM_WORKFLOW_DOMAIN") or "m.pipedream.net"

        if access_token:
            super().__init__(
                base_url=resolved_base_url,
                project_environment=project_environment,
                project_id=project_id,
                token=(lambda: access_token),
                timeout=timeout,
            )
        else:
            super().__init__(
                base_url=resolved_base_url,
                project_environment=project_environment,
                project_id=project_id,
                client_id=client_id,
                client_secret=client_secret,
                timeout=timeout,
            )

        self.workflows = AsyncWorkflowsClient(
            client_wrapper=self._client_wrapper,
            workflow_domain=resolved_workflow_domain,
        )

    @property
    def raw_access_token(self) -> Optional[str]:
        """
        Returns an access token that can be used to authenticate API requests
        """
        return self._client_wrapper._get_token()
