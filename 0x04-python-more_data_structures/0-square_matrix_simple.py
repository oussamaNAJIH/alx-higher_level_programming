#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix[0])
    matrix2 = []
    for row in matrix:
        row2 = []
        for i in range(0, length):
            row2.append(row[i] ** 2)
        matrix2.append(row2)
    return matrix2
