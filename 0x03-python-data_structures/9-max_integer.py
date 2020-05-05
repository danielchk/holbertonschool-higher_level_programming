#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        i = my_list[0]
        for run in my_list:
            if run >= i:
                i = run
        return i
    else:
        return None
