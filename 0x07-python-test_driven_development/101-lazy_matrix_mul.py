#!/usr/bin/python3
"""
multiply 2 matricies using numpy module.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that is given
    Args:
        m_a: input 1st matrix
        m_b: input 2nd matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
