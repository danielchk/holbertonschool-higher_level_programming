#!/usr/bin/python3
"""defines a square with size"""


class Square:
    """square with size
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): size of a square
        """
        self.size = size

    def area(self):
        """return area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """size self
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set a vakue for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """print the square whit #
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
