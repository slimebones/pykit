"""
Additional utils for error handling.
"""
from typing import Any, Never, NoReturn
from antievil._main import LogicError


def stringify(value: dict, separator: str = ", ") -> str:
    """
    Transforms dictionary into string representation.
    """
    option_strs: list[str] = []

    for k, v in value.items():
        option_strs.append(f"{k}={v}")

    return separator.join(option_strs)


def get_titled_value(
    title: str,
    value: Any | None = None,
) -> str:
    titled_value: str = title
    if value:
        titled_value = f"{title} <{value!s}>"

    return titled_value


def never(_: Never) -> NoReturn:
    error_message: str = "unhandled case"
    raise LogicError(error_message)