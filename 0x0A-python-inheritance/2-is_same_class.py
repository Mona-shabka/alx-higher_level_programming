#!/usr/bin/python3
"""Checks if object is instance of a class"""


def is_same_class(obj, a_class):
    """Method that return true if object is instance of
    class, otherwise return false
    """
    return (type(obj) == a_class)
