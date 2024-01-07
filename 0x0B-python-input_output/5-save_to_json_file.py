#!/usr/bin/python3
"""module to saving obj file"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file: function to save obj ot file
    """
    son = json.dumps(my_obj)
    with open(filename, mode='w', encoding="utf-8") as myFile:
        myFile.write(son)
