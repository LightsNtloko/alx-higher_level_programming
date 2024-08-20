def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda k: k ** 2, row)), matrix))
