#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    sub = ""
    for aim in str:
        if i != n:
            sub += aim
        i += 1
    return (sub)