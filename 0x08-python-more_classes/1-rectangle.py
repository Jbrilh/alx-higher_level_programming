#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """rectangle class initialization"""

        self.__width = width
        self.__height = height

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """set height with value
        Args:
            value: value of the height, must be a positive int
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """set the width value
        Args:
        value: value of the width, must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
