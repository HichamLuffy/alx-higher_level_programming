#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_dictionary = a_dictionary.copy()
    for key, value in cpy_dictionary.items():
        cpy_dictionary[key] = value * 2
    return cpy_dictionary