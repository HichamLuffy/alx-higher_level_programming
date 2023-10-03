#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """Return the matrix divided by a number.
    
    Args:
        matrix (list): The matrix to divide.
        div (int): The number to divide by.
    Raises:
        TypeError: If div is not an integer.
        ZeroDivisionError: If div is 0.
        TypeError: If matrix is not a matrix (list of lists)
        TypeError: If each row of the matrix is not of the same size
    Return:
        A new matrix divided by div
    """
    new_matrix = []
    if not isinstance(div, int):
        raise TypeError("div must be an integer")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, int) or isinstance(ele, float)
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)
    return new_matrix
