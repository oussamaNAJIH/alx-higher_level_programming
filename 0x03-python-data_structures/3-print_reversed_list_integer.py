#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        reversed_list = my_list.reverse()
    for i in reversed_list:
        print("{:d}".format(i))
