#!/usr/bin/python3
"""Defines read file module"""


def write_file(filename="", text=""):
    """
    write file: function to right a file
    prints the number of chars added
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)

    return len(text)
