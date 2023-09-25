#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        while x > 0:
            print("{:d}".format(my_list[j]), end='')
            j += 1
            x -= 1
        print("")
        return j
    except IndexError:
        return False
