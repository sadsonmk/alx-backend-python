#!/usr/bin/env python3
"""This is a module for adding type annotations to a function"""


from typing import Mapping, Union, Any, TypeVar, Callable
T = TypeVar('T', bound=Callable[..., Any])


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> \
        Union[Any, T]:
    """a function to apply type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
