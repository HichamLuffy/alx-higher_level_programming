#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence is False:
        return length, None
    return length, sentence[0]
