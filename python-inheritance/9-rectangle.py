#!/usr/bin/python3
"""just doc"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """just a Rectangle"""

    def __init__(self, width, height):
        """Comment"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implementation of area method"""
        return self.__width * self.__height

    def __str__(self):
        """to Print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
