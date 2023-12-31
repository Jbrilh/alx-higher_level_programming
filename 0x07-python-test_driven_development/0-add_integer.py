#!/usr/bin/python3
"""0-add_integer
The function "add_integer" returns the sum of two integers.
Args:
    a, b (int): integers values to be added
"""


def add_integer(a, b=98):
    """adds two integers function body
    Args:
        a, b (int) integer values """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
