#!/usr/bin/python3
"""Magic calculation module"""
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """Does a magic calculation"""
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
