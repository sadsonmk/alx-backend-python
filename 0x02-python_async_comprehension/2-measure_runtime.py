#!/usr/bin/env python3
"""This is the module for coroutine that will execute
   async_comprehension four times in parallel using asyncio.gather
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the total runtime of a function using asyncio.gather"""
    start = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            )
    end = time.time()
    return end - start
