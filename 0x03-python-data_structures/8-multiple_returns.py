#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        return 0
    length = len(sentence)
    first = sentence[0]
    return length, first
