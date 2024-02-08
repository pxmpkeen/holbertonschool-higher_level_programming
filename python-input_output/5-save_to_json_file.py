#!/usr/bin/python3
"""JSON"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as fd:
        fd.write(json.loads(my_obj))
