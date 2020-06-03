#!/usr/bin/python3
"""
module with function
"""


def write_file(filename="", text=""):
    """
    write in file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(str(text)))
