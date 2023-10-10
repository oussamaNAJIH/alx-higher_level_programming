#!/usr/bin/python3
"""
This module for Input/Output
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        characters_added = f.write(text)
    return characters_added
