#!/usr/bin/env python3
"""This is a module for a type-annotated function
   make_multiplier that takes a float multiplier as
   argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that takes a float multiplier and returns a function
       that multiplies a float by multiplier
    """
    return lambda num: num * multiplier
