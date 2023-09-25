#!/usr/bin/python3
def safe_print_integer(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
    except ValueError:
        print(value)
        return False
    return True
