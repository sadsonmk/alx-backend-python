#!/usr/bin/env python3
"""This is a module for calling task_wait_random"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a function that utilizes wait_random from another module to return a
       list of random floating point numbers
    """
    result = [task_wait_random(max_delay) for _ in range(n)]
    tasks_delay = []
    for future_task in asyncio.as_completed(result):
        task_delay = await future_task
        tasks_delay.append(task_delay)
    return tasks_delay
