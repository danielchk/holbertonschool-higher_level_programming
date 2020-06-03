#!/usr/bin/python3
"""
add arguments to a phyton list
"""

from sys import argv
save_to_json = __import__("7-save_to_json_file").save_to_json_file
load_from_json = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_file = load_from_json(filename)
except:
    json_file = []

for arg in argv[1:]:
    json_file.append(arg)

save_to_json(json_file, filename)
