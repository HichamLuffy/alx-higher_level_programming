#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    if tuple_a < 2 and tuple_b < 2:
        tuple_a += (0, 0)
        tuple_b += (0, 0)
    #for i in range(2):
    #    tuple_a += (0, 0)
    #    tuple_b += (0, 0)
    for i in range(len(tuple_a)):
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[i] + tuple_b[i],)
    return new_tuple