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

    def integer_validator(self, name, value):
        """
        value is int and exists
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
