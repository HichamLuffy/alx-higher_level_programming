#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """Print a square with the character #.
    Args:
        size (int): The size of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0
        TypeError: If size is a float
    Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
