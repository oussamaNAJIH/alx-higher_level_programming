#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
                formatted_item = "{:d}".format(my_list[i])
                if formatted_item.isdigit():
                    print(formatted_item, end="")
                    num_printed += 1
    except IndexError:
        pass
    print()
    return num_printed
