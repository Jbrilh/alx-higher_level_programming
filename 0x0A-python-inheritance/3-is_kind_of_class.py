#!/usr/bin/python3
"""Return instance of specified class of the parent of that class"""


def is_kind_of_class(obj, a_class):
    """function to return instance of a class
    Args:
        obj (any): the object to be compared
        a_class (type): the class that obj is compared to
    Returns:
        Bolean of an instance of a class
    """
    if isinstance(obj, a_class):
        return True
    return False
