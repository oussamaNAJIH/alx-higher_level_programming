#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    items = list(a_dictionary.items())
    best_key = items[0][0]
    best_value = items[0][1]
    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value

    return best_key
