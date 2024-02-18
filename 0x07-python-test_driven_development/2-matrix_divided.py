#!/usr/bin/python3
"""
    2-matrix_divided Module
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix

        Args:
            matrix: intial 2D list
            div: integer which is the divisor

        Returns:
            New matrix containing the divided elements
            rounded to 2 decimal places
    """
    prev_len = 0
    error_mess = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_mess)

    for b in matrix:    # matrix is a list
        if type(b) is not list:
            raise TypeError(error_mess)

        for e in b:
            if type(e) is not int and type(e) is not float:
                raise TypeError(error_mess)

        if len(b) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = len(b)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
