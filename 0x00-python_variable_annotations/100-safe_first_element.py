#!/usr/bin/env python3
"""This is a module augment code with the correct duck-typed annotations"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The function to correct duck-typed"""
    if lst:
        return lst[0]
    else:
        return None
