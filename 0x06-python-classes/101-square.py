#!/usr/bin/python3
"""square module."""


class Square:
    """define Square."""

    def __str__(self):
        """square"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Square.
        Args:
            size: square size.
            position: coordinates of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """square length.
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Square size.
        Args:
            value: size
        Raises:
                TypeError: if value is not int
                ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """square position.
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """square position.
        Args:
            value: if found.
        Raises:
                TypeError: if not tuple, positive.
        Returns: position.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """square area.
        Returns:
            size
        """
        return self.__size * self.__size

    def pos_print(self):
        """square position."""
        position = ""
        if not self.size:
            return "\n"
        for m in range(self.position[1]):
            position += "\n"
        for m in range(self.size):
            for x in range(self.position[0]):
                position += " "
            for y in range(self.size):
                position += "#"
            position += "\n"
        return position

    def my_print(self):
        """square."""
        print(self.pos_print(), end="")
