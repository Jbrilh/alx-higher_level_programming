#!/usr/bin/python3
"""class initalization"""


class Square:
    """Square class body"""

    def __init__(self, size=0, position=(0, 0)):
        """square constructor
        Args:
            size (int): the value of size
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """new size value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """this will set new value to size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """new size value"""
        return (self.__position)

    @position.setter
    def size(self, value):
        """this will set new value to size"""

        if not isinstance(value, tuple) \
                and len(value) == 2 \
                and all(isinstance(num, int) and num > 0 for num in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        """return the square of size"""
        return (self.__size * self.__size)

    def my_print(self):
        """print # using size"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
