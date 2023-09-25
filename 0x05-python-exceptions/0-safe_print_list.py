#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        list_copy = my_list.copy()
        while x > 0:
            print(list_copy[j], end='')
            j += 1
            x -= 1
        print(" ")
        return j
    
    except IndexError:
        print("")
    except Exception:
        print("other errors")
    return j