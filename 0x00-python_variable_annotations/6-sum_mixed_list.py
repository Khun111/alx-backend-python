#!/usr/bin/env python3
'''Module for typed annotation - sum_mixed_list'''
from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Function returns float from list'''
    count = 0
    for i in mxd_lst:
        count += i
    return (count)

