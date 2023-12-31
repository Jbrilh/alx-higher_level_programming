#!/usr/bin/python3
"""add integer class"""


def add_integer(a, b=98):
    """add intger class
    Args:
        a (int): value to be added
        b (int): value to be added also
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
