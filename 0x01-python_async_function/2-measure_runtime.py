#!/usr/bin/env python3
"""This is a module for measuring the runtime of a routine"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """a measure_time function with integers n and max_delay as arguments
       that measures the total execution time for wait_n(n, max_delay), and
       returns total_time / n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
