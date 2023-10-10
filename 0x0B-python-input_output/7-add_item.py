#!/usr/bin/python3
"""
This module for Input/Output
"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    existing_list = []
    for arg in sys.argv[1:]:
        existing_list.append(arg)
    save_to_json_file(existing_list, "add_item.json")
