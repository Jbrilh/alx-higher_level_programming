#!/usr/bin/python3
"""Square class that implements Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
            square class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """reurn width size
        """
        return self.width

    @size.setter
    def size(self, value):
        """module Square height and width
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Square class string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
