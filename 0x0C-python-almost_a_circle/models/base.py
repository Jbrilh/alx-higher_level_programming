#!/usr/bin/python3
"""module Base"""

import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor
        Args:
            id (int): integer value to id
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method to change list to dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "":
            return []

        return json.dumps(list_dictionaries)
