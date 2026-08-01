#!/usr/bin/python3
"""
This module provides a function that adds 2 integers.
It handles floats by casting them to integers first.
It raises TypeError for non-integer/float inputs.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Returns an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

