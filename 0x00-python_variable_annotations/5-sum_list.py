#!/usr/bin/env python3
'''Module for typed annotation - sum_list'''
from typing import List
def sum_list(input_list: List[float]) -> float:
    '''Function returns float from list'''
    count = 0
    for i in input_list:
        count += i
    return (count)

