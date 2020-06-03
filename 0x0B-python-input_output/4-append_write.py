#!/usr/bin/python3
"""
modeule with function
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as file:
        return (file.write(text))
