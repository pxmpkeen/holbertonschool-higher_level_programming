#!/usr/bin/python3
"""matrix division and test"""


def matrix_divided(matrix, div):
    """matrix division"""
    divisionerror = "division by zero"
    typeerror = "div must be a number"
    itemerror = "matrix must be a matrix (list of lists) of integers/floats"
    sizeerror = "Each row of the matrix must have the same size"

    def itemerrorfunc():
        raise TypeError(itemerror)

    def sizeerrorfunc():
        raise TypeError(itemerror)

    if int(div) == 0:
        raise ZeroDivisionError(divisionerror)
    elif not isinstance(div, (int, float)):
        raise TypeError(typeerror)

    length = len(matrix[0])
    return list(map(
        lambda x: list(map(
            lambda y: round(y / div, 2) if isinstance(
                y, (float, int)
                ) else itemerrorfunc(), x
            )) if len(x) == length else sizeerrorfunc(), matrix
        ))
