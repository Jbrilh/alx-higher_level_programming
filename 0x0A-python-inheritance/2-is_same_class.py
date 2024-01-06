#!/usr/bin/python3
"""function to chech objects similarity"""


def is_same_class(obj, a_class):
    """check if an obj is an istance of a given class.
    Args:
        obj (any): The objest to check.
        a_class (type): The class to compare the type of obj to.
    Returns:
        Boolean of an instance of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
