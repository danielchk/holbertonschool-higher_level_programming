#!/usr/bin/python3
"""
module with function
"""


def number_of_lines(filename=""):
    """
    Count the lines
    """
    i = 0

    with open(filename, encoding="utf-8") as file:
        for line in file:
            i += 1
    return (i)
