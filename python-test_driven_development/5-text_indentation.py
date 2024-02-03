#!/usr/bin/python3
"""prints text"""


def text_indentation(text):
    """func"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    for char in text:
        if char != ' ':
            flag = 1
        if flag == 1:
            print(char, end="")
