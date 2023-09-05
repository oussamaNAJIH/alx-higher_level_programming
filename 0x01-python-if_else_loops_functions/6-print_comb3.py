#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        number = "{}{}".format(i, j)
        if number == "89":
            print(number)
        else:
            print(number + ", ", end="")
