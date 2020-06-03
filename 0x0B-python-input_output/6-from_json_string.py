#!/usr/bin/python3
"""
module with a function
"""
import json


def from_json_string(my_str):
    """
    decoding in json
    """
    return (json.loads(my_str))
