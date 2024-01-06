#!/usr/bin/python3

"""Define square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Sqare class body"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
