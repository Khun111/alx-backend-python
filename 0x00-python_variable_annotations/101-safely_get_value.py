#!/usr/bin/env python3
'''Module for typed annotations'''
from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    '''Function for typed annotations'''
    if key in dct:
        return dct[key]
    else:
        return default
