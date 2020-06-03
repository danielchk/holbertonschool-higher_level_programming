#!/usr/bin/python3
"""
Module with function
"""


def read_lines(filename="", nb_lines=0):
    """read a number of lines"""
    i = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            i += 1
            print(line, end="")
            if nb_lines == i:
                break
