#!/usr/bin/python3
"""compare subclass"""


def inherits_from(obj, a_class):
    """ checks if obj is type of a_class
    Args:
        obj (any): input to be compare
        a_class (type): class obj is compared to
    Return:
        Boolean of the comparison
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
