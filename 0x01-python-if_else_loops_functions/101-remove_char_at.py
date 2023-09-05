#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n > length or n < 0:
        return str

    resultat = str[: n] + str[n + 1:]
    return resultat
