#!/usr/bin/python3
for number in range(100):
    if number == 99:
        print("{}".format(number))
    elif number < 10:
        print("{}{}, ".format(0, number), end="")
    else:
        print("{}, ".format(number), end="")
