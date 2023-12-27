#!/usr/bin/python3
"""Square class"""


class Square:
    """square class body"""

    def __init__(self, size=0):
        """square constructor
        Args:
            size (int): the value of size
        """
        self.__size = size

    @property
    def size(self):
        """return new size value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size to new value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return the value of the area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
