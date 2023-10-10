#!/usr/bin/python3
"""
This module for Input/Output
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    for arg in sys.argv[1:]:
        existing_list.append(arg)

    save_to_json_file(existing_list, "add_item.json")
