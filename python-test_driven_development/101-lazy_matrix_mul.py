#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices using NumPy.

>>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
array([[ 7, 10],
       [15, 22]])
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using NumPy and returns the result.

    >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    array([[13, 16]])
    """
    return np.matmul(m_a, m_b)
