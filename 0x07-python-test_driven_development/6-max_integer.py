#!/usr/bin/python3
"""max_integer module"""


def max_integer(list=[]):
    """Return the maximum integer in a list.
    
    Args:
        list (list): The list to search.
    Return:
        The maximum integer
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
