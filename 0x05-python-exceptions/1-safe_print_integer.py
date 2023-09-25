#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value)
        print("{:d}".format(value))
        
    except IndexError:
        print("")
    except Exception:
        print("{} is not an integer".format(value))
    return True
