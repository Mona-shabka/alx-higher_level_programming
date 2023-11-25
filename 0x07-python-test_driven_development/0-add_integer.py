#!/usr/bin/python3
"""add_integer module."""


def add_integer(a, b=98):
    """Adds two numbers.

    Args:
        a: 1st integer.
        b: 2nd integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The summation of two numbers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
