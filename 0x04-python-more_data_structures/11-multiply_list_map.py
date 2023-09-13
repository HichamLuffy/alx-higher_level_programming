#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    for i in my_list:
        mul = 0
        mul = i * number
        new_list.append(mul)
    return new_list
