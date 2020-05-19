#!/usr/bin/python3
"""defines a square with size"""


class Square:
    """
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of the square
        """
        self.size = size

    def area(self):
        """return square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size greater than zero
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
