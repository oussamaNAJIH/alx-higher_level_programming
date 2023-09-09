#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    length = len(my_list)
    if length == 0:
        return
    for i in range(length):
        if my_list[i] % 2 == 0:
            list2.append(True)
        else:
            list2.append(False)
    return list2
