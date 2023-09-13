#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy_list = my_list.copy()
    for i in range(len(cpy_list)):
        if cpy_list[i] == search:
            cpy_list[i] = replace
    return cpy_list
