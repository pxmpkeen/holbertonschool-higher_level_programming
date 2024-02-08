#!/usr/bin/python3
"""just doc"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """init of square class"""
        self.integer_validator("size", size)
        self.__width = self.__height = size

    def area(self):
        """Implementation of area method"""
        return self.__width * self.__height


s = Square(13)

print(s)
print(s.area())
