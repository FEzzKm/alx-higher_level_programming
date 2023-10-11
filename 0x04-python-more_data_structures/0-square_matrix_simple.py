#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """a function computes the square value of all int of matrix"""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
