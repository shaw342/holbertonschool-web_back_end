#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Write a type-annotated function sum_mixed_list which takes
    a list mxd_lst of integers and floats and returns their sum as a float. """
    result: float = 0
    for num in mxd_lst:
        result += num
    return result
