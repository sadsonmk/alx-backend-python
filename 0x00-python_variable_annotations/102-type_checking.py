#!/usr/bin/env python3
"""This is a module for using mypy to validate a piece of code"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This is a function that takes a tuple and an int and return a list"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
