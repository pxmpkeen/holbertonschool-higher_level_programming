#!/usr/bin/python3
"""Class MyList that inherits list"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        print(sorted(self))
