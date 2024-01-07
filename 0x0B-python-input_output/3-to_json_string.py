#!/usr/bin/python3
"""json rep"""


def to_json_string(my_obj):
    import json
    """
    to_json_string: function to convert my_obj to json
    returns json rep
    """
    return json.dumps(my_obj)
