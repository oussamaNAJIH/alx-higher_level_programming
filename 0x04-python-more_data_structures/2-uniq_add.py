#!/usr/bin/python3
def uniq_add(my_list=[]):
    list2 = set(my_list)
    sum = 0
    for i in list2:
        sum += i
    return sum
