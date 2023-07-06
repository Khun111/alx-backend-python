#!/usr/bin/env python3
'''Module for typed annotations'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Function to annotate'''
    if lst:
        return lst[0]
    else:
        return None
