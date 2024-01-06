#!/usr/bin/python3
"""import module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """squre class"""

    def __init__(self, size):
        """square class initiated"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area"""
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
