#!/usr/bin/env python3
"""This is a module for modifying a given function with appropriate
   annotations
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function taking an iterable sequence and return a list"""
    return [(i, len(i)) for i in lst]
