#!/usr/bin/python3
"""a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns the Python object with a JSON string"""
    return json.loads(my_str)
