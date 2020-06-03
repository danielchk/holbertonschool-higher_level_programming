#!/usr/bin/python3
import json
"""
module with a function
"""


def save_to_json_file(my_obj, filename):
    """
    function that represent in json an archive and save it
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
