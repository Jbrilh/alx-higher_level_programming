#!/usr/bin/python3
"""function to return list of available attributes"""


def lookup(obj):
    """Return a list of available attributes"""
    return dir(obj)
