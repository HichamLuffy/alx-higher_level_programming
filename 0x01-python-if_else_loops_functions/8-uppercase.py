#!/usr/bin/python3
def uppercase(str):
    rest_str = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            rest_str += chr(ord(c) - 32)
        else:
            rest_str += c
    print("{}".format(rest_str))
