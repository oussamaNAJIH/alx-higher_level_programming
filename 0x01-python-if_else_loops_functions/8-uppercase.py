#!/usr/bin/python3
def uppercase(input_str):
    for letter in input_str:
        uppercase_letter = letter
        if ord('a') <= ord(letter) <= ord('z'):
            uppercase_letter = chr(ord(letter) - ord('a') + ord('A'))
        print("{}".format(uppercase_letter), end="")
    print()