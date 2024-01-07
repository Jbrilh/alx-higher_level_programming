#!/usr/bin/python3
"""json to pyton objects"""
import json


def from_json_string(my_str):
    """
    from_json_string: function to change json to obj
    return that obj
    """
    return json.loads(my_str)
