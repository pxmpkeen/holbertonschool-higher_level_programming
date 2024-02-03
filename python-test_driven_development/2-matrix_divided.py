#!/usr/bin/python3
"""matrix division and test"""


def matrix_divided(matrix, div):
    """matrix division"""
    divisionerror = "division by zero"
    typeerror = "div must be a number"
    itemerror = "matrix must be a matrix (list of lists) of integers/floats"
    sizeerror = "Each row of the matrix must have the same size"

    if int(div) == 0:
        raise ZeroDivisionError(divisionerror)
    elif not isinstance(div, (int, float)):
        raise TypeError(typeerror)

    l = len(matrix[0])
    return list(map(
        lambda x: list(map(
            lambda y: round(y / div, 2) if isinstance(
                y, (float, int)
                ) else TypeError(itemerror), x
            )) if len(x) == l else TypeError(sizeerror), matrix
        ))
