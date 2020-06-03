#!/usr/bin/python3
"""
module with class student
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """student with 2 attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation of dictionaty of student class instance"""
        if attrs is None:
            return self.__dict__
        dict2 = {}
        for i in attrs:
            try:
                dict2[i] = self.__dict__[i]
            except:
                pass
        return dict2
