# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .configurable_prop import ConfigurableProp


class DeployedComponent(UniversalBaseModel):
    """
    A deployed component instance
    """

    id: str = pydantic.Field()
    """
    The unique ID of the deployed component
    """

    owner_id: str = pydantic.Field()
    """
    The ID of the owner
    """

    component_id: str = pydantic.Field()
    """
    The ID of the component that was deployed
    """

    configurable_props: typing.List[ConfigurableProp] = pydantic.Field()
    """
    The configurable properties of the component
    """

    configured_props: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    The configured properties of the component
    """

    active: bool = pydantic.Field()
    """
    Whether the deployed component is active
    """

    created_at: int = pydantic.Field()
    """
    The timestamp when the component was deployed (epoch milliseconds)
    """

    updated_at: int = pydantic.Field()
    """
    The timestamp when the component was last updated (epoch milliseconds)
    """

    name: str = pydantic.Field()
    """
    The name of the deployed component
    """

    name_slug: str = pydantic.Field()
    """
    The name slug of the deployed component
    """

    callback_observations: typing.Optional[typing.Optional[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
