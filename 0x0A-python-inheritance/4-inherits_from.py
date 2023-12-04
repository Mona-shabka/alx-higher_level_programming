#!/usr/bin/python3
"""checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """Method that returns true if object is instance of a class that inherited
    from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
