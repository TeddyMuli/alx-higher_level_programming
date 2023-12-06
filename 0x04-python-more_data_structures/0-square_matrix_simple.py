#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix =[[0 for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            square_matrix[i][j] = matrix[i][j] ** 2

    return square_matrix
