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

    def to_json(self):
        """respresentation of dict"""
        return self.__dict__
