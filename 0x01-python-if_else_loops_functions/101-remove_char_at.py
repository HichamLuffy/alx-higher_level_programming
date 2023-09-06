#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "" or n > len(str) - 1:
        return str
    cpy = ""
    for i in range(len(str)):
        if i != n:
            cpy += str[i]
    return cpy
