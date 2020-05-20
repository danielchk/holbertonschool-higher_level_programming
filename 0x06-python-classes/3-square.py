#!/usr/bin/python3
""" defines a square with size  """


class Square:
    """ square with size """

    def __init__(self, size=0):

        """
        Args:
            size (int): size of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
            """return square area
            """
            return (self.__size) ** 2
