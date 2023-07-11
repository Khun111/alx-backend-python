#!/usr/bin/env python3
'''Module for async_generator'''
import asyncio, random
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''Async function for async_comprehension'''
    return [i async for i in async_generator()]
