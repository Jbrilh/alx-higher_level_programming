#!/usr/bin/python3
"""square class definition"""


class Square:
    """class initial"""

    def __init__(self, size=0):
        """square class constructor
        Args
            size (int): the value of size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the new area of the square"""
        return (self.__size * self.__size)
