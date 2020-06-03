#!/usr/bin/python3
import json
"""
module with function
"""


def load_from_json_file(filename):
    """
    create a function from a json file
    """
    with open(filename) as file:
        obj = json.load(file)
    return (obj)
