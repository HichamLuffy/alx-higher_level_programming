#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    if idx == 0:
        my_list.remove(my_list[0])
    for i in my_list:
        if idx == i:
            my_list.remove(my_list[i])
    return my_list
