#!/usr/bin/python3
"""a string-to-JSON function"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string"""
    return json.dumps(my_obj)
