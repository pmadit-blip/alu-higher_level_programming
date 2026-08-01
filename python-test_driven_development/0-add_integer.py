#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.

>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, returns an integer.

    >>> add_integer(1, 2)
    3
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
