#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
signed_last_digit = last_digit
if number < 0:
    signed_last_digit = -signed_last_digit
print("Last digit of", number, "is", signed_last_digit, end="")
if signed_last_digit > 5:
    print(" and is greater than 5")
elif signed_last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
