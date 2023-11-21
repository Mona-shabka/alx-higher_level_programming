#!/usr/bin/python3
"""square module"""


class Square:
    """Define square"""

    def __init__(self, size=0):
        """square.
        Args:
            size: represnets square size.
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
