#!/usr/bin/python3
"""A square module"""


class Square:
    """defines square"""

    def __init__(self, size=0, position=(0, 0)):
        """Square
        Args:
            size: Square length.
            position: coordinates of square.
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"Square size.
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Square coordinates.
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """square position.
        Args: tuple value of two positive.
        Raises:
            TypeError: if value is not a tuple or < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Square area
        Returns: square size.
        """
        return self.__size * self.__size

    def pos_print(self):
        """position."""
        m_pos = ""
        if self.size == 0:
            return "\n"
        for m in range(self.position[1]):
            m_pos += "\n"
        for m in range(self.size):
            for n in range(self.position[0]):
                m_pos += " "
            for x in range(self.size):
                m_pos += "#"
            m_pos += "\n"
        return m_pos

    def my_print(self):
        """square position"""
        print(self.pos_print(), end='')
