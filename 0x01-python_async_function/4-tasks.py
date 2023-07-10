#!/usr/bin/env python3
'''Module for task_wait_n'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Async function for task_wait_n'''
    tasks = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(tasks)
