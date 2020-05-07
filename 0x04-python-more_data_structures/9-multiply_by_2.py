#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = dict()

    for i, j in a_dictionary.items():
        mult[i] = j * 2
    return mult
