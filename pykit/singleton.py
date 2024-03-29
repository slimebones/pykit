from __future__ import annotations

from typing import Any, TypeVar

SingletonInstance = TypeVar("SingletonInstance")

class SingletonMeta(type):
    """Singleton metaclass for implementing singleton patterns.

    See:
        https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    """
    __instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]

    def try_discard(cls) -> bool:
        try:
            del cls.__instances[cls]
        except KeyError:
            return False
        return True

class Singleton(metaclass=SingletonMeta):
    """Singleton base class."""
    @classmethod
    def ie(cls: type[SingletonInstance]) -> SingletonInstance:
        """Gets the single instance of the Singleton.

        Returns:
            Instance the Singleton holds.
        """
        return cls()
