#!/usr/bin/python3
def uppercase(str):
    rest_str = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            rest_str += chr(ord(c) - 32)
        else:
            rest_str += c
    return rest_str

    for alpha in range(ord('z'), ord('a') - 1, -1):
        if alpha % 2 != 0:
            alpha = ord(uppercase(chr(alpha)))
        print("{}".format(chr(alpha)), end="")
