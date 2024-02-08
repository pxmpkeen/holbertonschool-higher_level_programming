#!/usr/bin/python3
"""JSON"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

list_of_args = sys.args[1:]
save_to_json_file(list_of_args, filename)
load_from_json_file(filename)
