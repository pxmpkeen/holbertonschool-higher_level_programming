#!/usr/bin/python3
"""
Inheriting Square from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of object"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """toStr method"""
        sId = "[Square] ({}) ".format(self.id)
        return sId + "{}/{} - {}".format(self.x, self.y, self.size)

    @property
    def size(self):
        """Size getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.__width = value
        self.__height = value
