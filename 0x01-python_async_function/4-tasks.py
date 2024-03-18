#!/usr/bin/env python3
"""This is a module for calling task_wait_random"""


import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a function that utilizes wait_random from another module to return a
       list of random floating point numbers
    """
    result = [wait_n(max_delay) for _ in range(n)]
    tasks_delay = []
    for future_task in asyncio.as_completed(result):
        task_delay = await future_task
        tasks_delay.append(task_delay)
    return tasks_delay
