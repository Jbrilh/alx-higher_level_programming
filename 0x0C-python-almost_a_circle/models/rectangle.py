#!/usr/bin/python3
"""Rectangle class implement Base class """


from models.base import Base


class Rectangle(Base):
    """ rectangle class implement Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Returning private attribute (__width)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setting private attribute (__width)
        """
        self.validator('width', value)
        self.__width = value

    @property
    def height(self):
        """
            Returning private attribute (___height)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setting private attribute (__height)
        """
        self.validator('height', value)
        self.__height = value

    @property
    def x(self):
        """
            Returning private attribute (__x)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setting private attribute (__x)
        """
        self.validator('x', value)
        self.__x = value

    @property
    def y(self):
        """
            Returning private attribute (__y)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setting private attribute (__y)
        """
        self.validator('y', value)
        self.__y = value

    @staticmethod
    def validator(attribute, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attribute))
        elif value <= 0:
            raise ValueError('{} must be > 0'.format(attribute))

    def area(self):
        """
            function to return the area
        """
        return (self.__width * self.__height)

    def display(self):
        """
            function to display the rectangle with #
        """
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")
