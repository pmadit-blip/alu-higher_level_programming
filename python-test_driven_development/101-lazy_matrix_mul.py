#!/usr/bin/python3
"""101-lazy_matrix_mul"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        Result of matrix multiplication
    """
    return np.matmul(m_a, m_b)
