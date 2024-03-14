#!/usr/bin/env python3
"""This is a module for a type-annotated function
   to_kv that takes a string k and an int OR float
   v as arguments and returns a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a function that takes a string and a union of float or int and combine
       into a tuple
    """
    return (k, v**2)
