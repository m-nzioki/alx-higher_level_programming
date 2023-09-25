#!/usr/bin/python3

"""A matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements os a matrix

    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): Divisor
    Raises:
        TypeError if:
            matrix is not a list of lists of integers or floats
            Each row of the matrix is not the same size
            div is not either an int or float
        ZeroDivisionError: If div is 0

    Returns a new matrix with the quotients
    """

    if not all(isinstance(row, list) and
            all(isinstance(val, (int, float)) for val in row)\
                    for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
