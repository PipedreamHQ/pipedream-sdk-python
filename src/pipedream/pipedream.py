import os
from typing import Optional

from .client import (
    AsyncClient,
    Client,
)
from .environment import PipedreamEnvironment
from .types.project_environment import ProjectEnvironment


class Pipedream(Client):

    def __init__(
        self,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        project_id: Optional[str] = None,
        project_environment: ProjectEnvironment = "production",
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
    ):
        project_id = project_id or os.getenv("PIPEDREAM_PROJECT_ID")
        if not project_id:
            raise ValueError("Project ID is required")

        super().__init__(
            base_url=_get_base_url(environment),
            client_id=client_id,
            client_secret=client_secret,
            project_id=project_id,
            project_environment=project_environment,
        )


class AsyncPipedream(AsyncClient):

    def __init__(
        self,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        project_id: Optional[str] = None,
        project_environment: ProjectEnvironment = "production",
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
        **kwargs,
    ):
        project_id = project_id or os.getenv("PIPEDREAM_PROJECT_ID")
        if not project_id:
            raise ValueError("Project ID is required")

        super().__init__(
            base_url=_get_base_url(environment),
            client_id=client_id,
            client_secret=client_secret,
            project_id=project_id,
            project_environment=project_environment,
            **kwargs,
        )


def _get_base_url(environment: PipedreamEnvironment) -> str:
    """
    Returns the base URL for the given environment.
    """
    return os.path.expandvars(environment.value)
