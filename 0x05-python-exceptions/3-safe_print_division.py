#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("inside result: {}".format(c))
    return c
