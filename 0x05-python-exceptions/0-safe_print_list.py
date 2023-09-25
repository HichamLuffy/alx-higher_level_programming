#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        while x > 0:
            print("{}".format(my_list[j]), end='')
            j += 1
            x -= 1
        print(" ")
    except IndexError:
        print("")
    except Exception:
        print("other errors")
    return j
