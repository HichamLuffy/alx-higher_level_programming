#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_matrix = [list(row) for row in matrix]
    for i in cpy_matrix:
        for j in range(len(i)):
            i[j] = i[j] ** 2
    return cpy_matrix
