#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    length = len(sentence)
    if length == 0:
        first_char = None
    first_char = sentence[0]
    my_tuple = length, first_char
    return my_tuple
