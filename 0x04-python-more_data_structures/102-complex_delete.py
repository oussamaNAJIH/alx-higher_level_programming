#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    for key in list_keys:
        if a_dictionary.get(key) == value:
            a_dictionary.pop(key)
    return a_dictionary
