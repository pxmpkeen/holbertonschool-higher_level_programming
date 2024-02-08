#!/usr/bin/python3
"""Define a class"""


class Student:
    """Class Student"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Initialization of object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attr is None:
            return self.__dict__
        res = {}
        for i in attrs:
            if i in self.__dict__:
                res[i] = self.__dict__[i]
        return res
