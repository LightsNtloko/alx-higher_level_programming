#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    new_matrix = [[k**2 for k in row] for row in matrix]
    return new_matrix
