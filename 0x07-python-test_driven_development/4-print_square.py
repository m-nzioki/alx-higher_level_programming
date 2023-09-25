#!/usr/bin/python3

"""Defines a square printing function"""


def print_sqaure(size):
    """Prints squares using the # character
    Args:
        size(int): legth of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
