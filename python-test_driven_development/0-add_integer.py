#!/usr/bin/python3
"""adding ints and testing"""


def add_integer(a, b=98):
    """adding ints"""
    if isinstance(a, (int, float)) == False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) == False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
