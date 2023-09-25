#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        inside = a / b
    except (TypeError, ZeroDivisionError):
        inside = None
    finally:
        print("inside result = {}".format(inside))
    return inside
