#!/usr/bin/python3
"""IO tasks"""


def read_file(filename=""):
    """Reads file"""
    with open(filename, 'w', encoding="utf-8") as fd:
        r = fd.read()
        print(r)
