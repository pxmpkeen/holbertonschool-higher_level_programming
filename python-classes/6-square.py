#!/usr/bin/python3
"""Declare class Square"""


class Square:
    """Square class with a private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        self.__position = value
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position[0], int) or self.__position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position[1], int) or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self) -> int:
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
