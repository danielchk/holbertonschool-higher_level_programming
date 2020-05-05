#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divs = []
    for run in my_list:
        if run % 2 == 0:
            divs.append(True)
        else:
            divs.append(False)
    return divs
