#!/usr/bin/python3
"""
module with class 
"""


class BaseGeometry:
    """
    class Base has 2 public instances
    """
    def area(self):
        """
        Raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate if value is int and exist
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        instantiation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):

        return (self.__width * self.__height)

    def __str__(self):
        """
        Representation of the rectangle in a string
        """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
