#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_value = list(a_dictionary.values())
    list_keys = list(a_dictionary.keys())
    if value not in list_value:
        return a_dictionary
    i = list_value.index(value)
    key = list_keys[i]
    a_dictionary.pop(key)
    return a_dictionary
