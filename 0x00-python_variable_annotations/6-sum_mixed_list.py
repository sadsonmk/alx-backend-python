#!/usr/bin/env python3
"""This is a module for a type-annotated function
   sum_mixed_list which takes a list mxd_lst of integers
   and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that takes floats and ints and return their sum as float"""
    total: float = 0
    for num in mxd_lst:
        total += num
    return total
