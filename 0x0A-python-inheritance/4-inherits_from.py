#!/usr/bin/python3
"""
module
"""


def inherits_from(obj, a_class):
    """why this don't work?"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
