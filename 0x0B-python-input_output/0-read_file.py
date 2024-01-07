#!/usr/bin/python3
"""function to read file"""


def read_file(filename=""):
    """reading func"""
    with open(filename, 'r', encoding="utf-8") as myFile:
        print(myFile.read())
