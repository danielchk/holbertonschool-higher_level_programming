#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        lenfirst = (len(sentence), sentence[0])
    else:
        lenfirst = (0, None)
    return lenfirst
    