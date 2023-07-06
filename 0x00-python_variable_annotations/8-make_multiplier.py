#!/usr/bin/env python3
'''Module for typed annotation - make_multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Function returns tuple from str and int/float'''
    return (lambda x: x * multiplier)
