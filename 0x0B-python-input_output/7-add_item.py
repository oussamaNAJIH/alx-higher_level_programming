#!/usr/bin/python3
"""
This script takes command-line arguments and adds them to a Python list,
then saves the list to a file in JSON format.

Usage:
    ./7-add_item.py [arg1] [arg2] [arg3] ...

The script will create a file named "add_item.json" to store the list.
If the file already exists, it will append the new arguments to the existing list.

Example:
    ./7-add_item.py Best School
    ./7-add_item.py 89 Python C
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

for arg in sys.argv[1:]:
    existing_list.append(arg)

save_to_json_file(existing_list, "add_item.json")
