#!/usr/bin/python3
"""this module defines a class MyInt that inherits from integer."""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == opeartor with != behaviour"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behaviour"""
        return self.real == value
