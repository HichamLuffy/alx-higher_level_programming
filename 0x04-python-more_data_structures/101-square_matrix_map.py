#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    cpy_matrix = [list(row) for row in matrix]
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), cpy_matrix))
