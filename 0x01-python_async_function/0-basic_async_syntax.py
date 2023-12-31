#!/usr/bin/env python3
'''Module for wait_random'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Function for wait_random'''
    range_wait = random.uniform(0, max_delay)
    await asyncio.sleep(range_wait)
    return (range_wait)
