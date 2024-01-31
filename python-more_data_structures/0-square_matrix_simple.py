#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
c = square_matrix_simple(matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print(c)
