#!/usr/bin/env python3
"""This is a module for a coroutine that will collect 10 random numbers using
   an async comprehensing over async_generator, then return the
   10 random numbers.
"""


import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """a function that takes an async generator and return numbers generated
       using a comprehension
    """
    comp = [x async for x in async_generator()]
    return comp
