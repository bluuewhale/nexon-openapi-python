from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Tuple, Type, TypeVar, cast, Union
from datetime import date, datetime

import pydantic
from pydantic.fields import FieldInfo

from ._types import StrBytesIntFloat


_ModelT = TypeVar("_ModelT", bound=pydantic.BaseModel)

PYDANTIC_V2 = pydantic.VERSION.startswith("2.")

# v1 re-exports
if TYPE_CHECKING:

    def parse_date(value: Union[date, StrBytesIntFloat]) -> date:  # noqa: ARG001
        ...

    def parse_datetime(value: Union[datetime, StrBytesIntFloat]) -> datetime:  # noqa: ARG001
        ...

    def get_args(t: Type[Any]) -> Tuple[Any, ...]:  # noqa: ARG001
        ...

    def is_union(tp: Optional[Type[Any]]) -> bool:  # noqa: ARG001
        ...

    def get_origin(t: Type[Any]) -> Optional[Type[Any]]:  # noqa: ARG001
        ...

    def is_literal_type(type_: Type[Any]) -> bool:  # noqa: ARG001
        ...

    def is_typeddict(type_: Type[Any]) -> bool:  # noqa: ARG001
        ...

else:
    if PYDANTIC_V2:
        from pydantic.v1.typing import get_args as get_args
        from pydantic.v1.typing import is_union as is_union
        from pydantic.v1.typing import get_origin as get_origin
        from pydantic.v1.typing import is_typeddict as is_typeddict
        from pydantic.v1.typing import is_literal_type as is_literal_type
        from pydantic.v1.datetime_parse import parse_date as parse_date
        from pydantic.v1.datetime_parse import parse_datetime as parse_datetime
    else:
        from pydantic.typing import get_args as get_args
        from pydantic.typing import is_union as is_union
        from pydantic.typing import get_origin as get_origin
        from pydantic.typing import is_typeddict as is_typeddict
        from pydantic.typing import is_literal_type as is_literal_type
        from pydantic.datetime_parse import parse_date as parse_date
        from pydantic.datetime_parse import parse_datetime as parse_datetime


# refactored config
if TYPE_CHECKING:
    from pydantic import ConfigDict as ConfigDict
else:
    if PYDANTIC_V2:
        from pydantic import ConfigDict
    else:
        # TODO: provide an error message here?
        ConfigDict = None


# renamed methods / properties
def parse_obj(model: Type[_ModelT], value: object) -> _ModelT:
    if PYDANTIC_V2:
        return model.model_validate(value)
    else:
        return cast(_ModelT, model.model_validate(value))  # pyright: ignore[reportDeprecated, reportUnnecessaryCast]


def field_is_required(field: FieldInfo) -> bool:
    if PYDANTIC_V2:
        return field.is_required()
    return field.is_required  # type: ignore


def field_get_default(field: FieldInfo) -> Any:
    value = field.get_default()
    if PYDANTIC_V2:
        from pydantic_core import PydanticUndefined

        if value == PydanticUndefined:
            return None
        return value
    return value


def field_outer_type(field: FieldInfo) -> Any:
    if PYDANTIC_V2:
        return field.annotation
    return field.outer_type_  # type: ignore


def get_model_config(model: Type[pydantic.BaseModel]) -> Any:
    if PYDANTIC_V2:
        return model.model_config
    return model.__config__  # type: ignore


def get_model_fields(model: Type[pydantic.BaseModel]) -> Dict[str, FieldInfo]:
    if PYDANTIC_V2:
        return model.model_fields
    return model.__fields__  # type: ignore


def model_copy(model: _ModelT) -> _ModelT:
    if PYDANTIC_V2:
        return model.model_copy()
    return model.copy()  # type: ignore


def model_json(model: pydantic.BaseModel, *, indent: Optional[int] = None) -> str:
    if PYDANTIC_V2:
        return model.model_dump_json(indent=indent)
    return model.json(indent=indent)  # type: ignore


def model_dump(
    model: pydantic.BaseModel,
    *,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
) -> Dict[str, Any]:
    if PYDANTIC_V2:
        return model.model_dump(
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
        )
    return cast(
        "dict[str, Any]",
        model.dict(  # pyright: ignore[reportDeprecated, reportUnnecessaryCast]
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
        ),
    )


def model_parse(model: Type[_ModelT], data: Any) -> _ModelT:
    if PYDANTIC_V2:
        return model.model_validate(data)
    return model.parse_obj(data)  # pyright: ignore[reportDeprecated]


# generic models
if TYPE_CHECKING:

    class GenericModel(pydantic.BaseModel):
        ...

else:
    if PYDANTIC_V2:
        # there no longer needs to be a distinction in v2 but
        # we still have to create our own subclass to avoid
        # inconsistent MRO ordering errors
        class GenericModel(pydantic.BaseModel):
            ...

    else:
        import pydantic.generics

        class GenericModel(pydantic.generics.GenericModel, pydantic.BaseModel):
            ...
