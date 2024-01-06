#!/usr/bin/python3
"""my list class inherits form list"""


class MyList(list):
    """my list class to return list in order"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
