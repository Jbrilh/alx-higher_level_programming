#!/usr/bin/python3
"""text appending module"""


def append_write(filename="", text=""):
    """
    append_write: function to append the text
    returns the number of texts to be appended
    """
    with open(filename, mode='a', encoding="utf-8") as myFile:
        myFile.write(text)

    return len(text)
