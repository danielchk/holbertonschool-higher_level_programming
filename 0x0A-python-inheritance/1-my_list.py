#!/usr/bin/python3
"""
Module that inherits in a list
"""


class MyList(list):
    """
    inherits in a list
    """
    def print_sorted(self):
        print(sorted(self))
