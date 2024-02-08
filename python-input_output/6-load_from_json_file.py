#!/usr/bin/python3
"""JSON"""
import json


def save_to_json_file(my_obj, filename):
    """JSON -> text -> file"""
    with open(filename, 'r') as fd:
        fd.write(json.loads(my_obj))
