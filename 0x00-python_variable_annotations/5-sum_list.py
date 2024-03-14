#!/usr/bin/env python3
"""This is a module for a type-annotated function sum_list
   which takes a list input_list of floats as argument and
   returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """A function that takes a list of floats and sum them up"""
    total: float = 0
    for num in input_list:
        total += num
    return total
