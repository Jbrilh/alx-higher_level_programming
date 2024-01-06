#!/usr/bin/python3
"""Int class inverted"""


class MyInt(int):
    """my int class to invert values"""

    def __eq__(self, other):
        """override the == operator"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """override the != operator"""
        return not super().__ne__(other)
