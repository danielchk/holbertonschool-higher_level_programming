#!/usr/bin/python3
"""
Module with function
"""


def read_file(filename=""):
    """""reads a text file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
