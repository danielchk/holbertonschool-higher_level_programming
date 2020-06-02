#!/usr/bin/python3
"""
Module with a public instance
"""


class BaseGeometry:
    """
    super class
    """
    def area(self):
        """
        Raise exception
        """
        raise Exception("area() is not implemented")
