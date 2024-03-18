#!/usr/bin/env python3
"""This is a module for executing multiple routines with asyncio"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """a function that utilizes wait_random from another module to return a
       list of random floating point numbers
    """
    result = [wait_random(max_delay) for _ in range(n)]
    tasks_delay = []
    for future_task in asyncio.as_completed(result):
        task_delay = await future_task
        tasks_delay.append(task_delay)
    return tasks_delay
