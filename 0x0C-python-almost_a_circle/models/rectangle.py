#!/usr/bin/python3
"""Rectangle class implement Base class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class implements Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
            funciton to get width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
             function to set widht value
        """
        self.__width = value

    @property
    def height(self):
        """
            funciton to get height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            function to set height value
        """
        self.__height = value

    @property
    def x(self):
        """
            funciton to get height x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            function to set x value
        """
        self.__x = value

    @property
    def y(self):
        """funciton to get y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """function to set y value
        Args:
        value (int): value to set to y
        """
        self.__y = value
