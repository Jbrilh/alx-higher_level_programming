#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry:
    """Class body."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate values
        Args:
            name (string):string value
            value (int): integer value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
