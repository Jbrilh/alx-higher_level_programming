#!/usr/bin/python3
"""
    Rectangle class with print func
"""


class Rectangle:
    """rectangle class with width and height"""

    def __init__(self, width=0, height=0):
        """rectangle class initialized"""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns on infromal string representation
        """
        if self.__height == 0 or self.__width == 0:
            return ''

        rectangle_str = ''
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    @property
    def width(self):
        """function to get width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """function to set width value
        Args:
            value: the value to set the widht"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """function to get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """function to set the height value
        Args:
            value: value to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to calculate and return area"""
        return self.__width * self.__height

    def perimeter(self):
        """function to calculate and return primeter"""
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return perimeter
        preimeter = (self.__width + self.__height) * 2
