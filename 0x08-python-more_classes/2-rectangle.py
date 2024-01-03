#!/usr/bin/python3
"""
    Define rectangle class
"""


class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """
            Inintialize Rectangle class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """fucntion to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """function to set width with value
        Args:
            value: the value to be set to width"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """function to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function to set height value
        Args:
            value: the value to be set to height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to calculate and return the area"""
        return self.__width * self.__height

    def perimeter(self):
        """function to calculate and return the perimeter of rectangle"""
        perimeter = 0
        if self.__width == 0 or self.height == 0:
            return perimeter
        perimeter = (self.__width + self.__height) * 2
        return perimeter
