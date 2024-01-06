#!/usr/bin/python3
"""import module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """class initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area function to calculate"""
        return (self.__width * self.__height)

    def __str__(self):
        """string rep of the area"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
