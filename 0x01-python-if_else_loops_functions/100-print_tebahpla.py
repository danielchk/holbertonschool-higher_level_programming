#!/usr/bin/python3
for abc in range(122, 96, -1):
    if abc % 2 != 0:
        abc -= 32
    print("{}".format(chr(abc)), end="")
