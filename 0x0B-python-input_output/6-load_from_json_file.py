#!/usr/bin/python3
"""a JSON file-reading function"""


import json


def load_from_json_file(filename):
    """Creates a Python object from JSON file"""
    with open(filename) as f:
        return json.load(f)
