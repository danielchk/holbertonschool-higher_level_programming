#!/usr/bin/python3
""" class rectangle """


class Rectangle:
    """ rectangle and attributes width and height """

    def __init__(self, width=0, height=0):
        """
        Args:
            -width: width of rectangle
            -height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ width positive and int """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ height positive and int """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ area """
        return self.width * self.height

    def perimeter(self):
        """ perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string of the definition of a rectangle"""
        strg = ""
        if self.__width != 0 and self.__height != 0:
            strg += "\n".join("#" * self.__width for i in range(self.__height))
        return strg

    def __repr__(self):
        """string of the rectangle 2"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
