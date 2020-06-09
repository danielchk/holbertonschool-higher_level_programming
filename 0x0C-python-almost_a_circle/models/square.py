#!/usr/bin/python3
"""Module with class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """width and height are the same"""
        return(self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args):
            for num, value in enumerate(args):
                if num == 0:
                    self.id = value
                if num == 1:
                    self.width = value
                if num == 2:
                    self.height = value
                if num == 3:
                    self.x = value
                if num == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        dic2 = {}
        dic2["id"] = self.id
        dic2["width"] = self.width
        dic2["height"] = self.height
        dic2["x"] = self.x
        dic2["y"] = self.y
        return (dic2)
