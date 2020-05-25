#!/usr/bin/python3
"""
matrix_divided module
"""


def matrix_divided(matrix, div):
    """dividematrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = 0
    for each in matrix:
        if type(each) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is 0:
            size = len(each)
        elif size != len(each):
            raise TypeError("Each row of the matrix must have the same size")
        for elements in each:
            if type(elements) is not int and type(elements) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elements / div, 2) for elements in each] for each in matrix]
