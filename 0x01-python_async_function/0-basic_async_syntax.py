#!/usr/bin/env python3
'''Module for wait_random'''
import asyncio, random

async def wait_random(max_delay = 10):
    range_wait = random.uniform(0, max_delay)
    await asyncio.sleep(range_wait)
    return (range_wait)
'''
async def main():
    await wait_random()

asyncio.run(main())
'''