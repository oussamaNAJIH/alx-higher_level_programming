#!/usr/bin/python3
"""
This module is for dividing all elements of a matrix.
Functions:
    matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and round to 2 decimal places.
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) and
                    all(isinstance(i, (int, float)) for i in row)
                    for row in matrix):
        raise TypeError("matrix must be \
                        a matrix (list of lists) of integers/floats")

    num_cols = len(matrix[0])

    if not all(len(row) == num_cols for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)

    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")