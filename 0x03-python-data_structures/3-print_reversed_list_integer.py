#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        length = len(my_list)
        for i in my_list[-1:-length-1:-1]:
            print("{:d}".format(i))
