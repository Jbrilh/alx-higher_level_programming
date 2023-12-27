#!/usr/bin/python3
"""square class definition"""


class Square:
    """class initial"""

    def __init__(self, size):
        """square class constructor
        Args
            size (int): the value of size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")

        self.__size = size

    def area(self):
        return (self.__size * self.__size)
