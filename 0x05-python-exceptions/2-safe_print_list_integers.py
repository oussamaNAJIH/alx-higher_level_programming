#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    for i in range (x):
        try:
            formated_item = "{:d}".format(my_list[i])
            print(formated_item, end="")
            num_printed+=1
        except (ValueError, TypeError):
            continue
    print()
    return num_printed
