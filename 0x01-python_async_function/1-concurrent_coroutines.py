#!/usr/bin/env python3
"""This is a module for executing multiple routines with asyncio"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """a function that utilizes wait_random from another module to return a
       list of random floating point numbers
    """
    result = []
    for x in range(n):
        result.append(await wait_random(max_delay))
    return result
