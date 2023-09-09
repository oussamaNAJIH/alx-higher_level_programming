#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    else:
        copy_list = my_list.copy()
        copy_list[idx] = element
        return copy_list
