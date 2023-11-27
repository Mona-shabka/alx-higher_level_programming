#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):
        """rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
