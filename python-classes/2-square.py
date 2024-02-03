#!/usr/bin/python3
"""Declare class Square"""


class Square:
    """Square class with a private attribute"""
    def __init__(self, size=0):
        self.__size = int(size)
        if not isinstance(size, int):
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")
