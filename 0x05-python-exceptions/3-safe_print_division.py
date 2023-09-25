#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        inside = a / b
        print("Inside result: = {:.2f}".format(inside))
        return inside
    except (TypeError, ZeroDivisionError):
        print("Inside result: = None")
        return None
