#!/usr/bin/python3
"""checks if object is instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Method that returns true if object is instance of a class
    or inherits class.
    """
    return (isinstance(obj, a_class))
