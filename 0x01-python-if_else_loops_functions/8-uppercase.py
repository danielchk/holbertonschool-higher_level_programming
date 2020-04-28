#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = ord(c) - 32
            upper += chr(c)
        else:
            upper += c
    print("{}".format(upper), end="")
    print("")
