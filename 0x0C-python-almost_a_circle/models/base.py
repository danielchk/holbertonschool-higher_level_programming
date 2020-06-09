#!/usr/bin/python3
"""
Module with Base class
"""
import json


class Base:

    """Base class with  a private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        funct = cls.__name__ + ".json"
        objs = []
        if list_objs is not None:
            for i in list_objs:
                objs.append(cls.to_dictionary(i))
        with open(funct, mode="w") as myFile:
            myFile.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ is "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return (temp)

    @classmethod
    def load_from_file(cls):
        funct = cls.__name__ + ".json"
        inst = []
        try:
            with open(funct, mode="r") as myFile:
                inst = cls.from_json_string(myFile.read())
            for i, j in enumerate(inst):
                inst[i] = cls.create(**inst[i])
        except:
            pass
        return (inst)

    @classmethod
    def load_from_file_csv(cls):
        try:
            fn = cls.__name__ + ".csv"
            with open(fn, newline="") as myFile:
                reader = csv.DictReader(myFile)
                lst = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    lst.append(x)
                return ([cls.create(**objt) for objt in lst])
        except FileNotFoundError:
            return ([])

    @classmethod
    def load_from_file_csv(cls):
