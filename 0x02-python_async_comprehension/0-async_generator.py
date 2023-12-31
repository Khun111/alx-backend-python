#!/usr/bin/env python3
'''Module for async_generator'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Async function for async_generator'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
