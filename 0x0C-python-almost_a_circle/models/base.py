#!/usr/bin/python3
"""module Base"""


class Base:
    """Base class"""

__nb_objects = 0
    def __init__(self, id=None):
        """Base class constructor
        Args:
            id (int): integer value to id
        """
        if id not None:
            self.__id = id


