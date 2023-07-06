#!/usr/bin/env python3
'''Module for typed annotation - to_kv'''
from typing import Union, Tuple
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Function returns tuple from str and int/float'''
    return (k, v**2)

