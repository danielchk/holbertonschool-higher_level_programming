#!/usr/bin/python3
"""
5-text_indentation
"""


def text_indentation(text):
    """
    print a text and leave 2 new line aftes special symbols
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    space = 0

    for i in text:
        if space == 0:
            if i == ' ':
                continue
            else:
                space = 1
        if space == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                space = 0
            else:
                print(i, end="")
