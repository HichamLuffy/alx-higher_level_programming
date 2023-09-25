#!/usr/bin/python3

def magic_calculation(a, b):
    rslt = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            rslt += a ** b / i
        except Exception:
            rslt = b + a
            break
    return rslt