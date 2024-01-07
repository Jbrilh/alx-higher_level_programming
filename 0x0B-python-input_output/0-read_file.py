#!/usr/bin/python3
"""function to read file"""


def read_file(filename=""):
    """
    read_file function
    reads a text file (UTF-8) and prints its result to stdout
    """
    with open(filename, mode='r', encoding="utf-8") as myFile:
        print(myFile.read(), end='')
