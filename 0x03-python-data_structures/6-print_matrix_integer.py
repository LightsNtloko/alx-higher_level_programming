#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:  # Handle empty matrix case
        return
    
    for row in matrix:
        print(' '.join("{:d}".format(num) for num in row))
