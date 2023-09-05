#!/usr/bin/python3
def magic_calculation(a, b, c):
    if c > b:
        resultat = a + b
        return resultat
    elif a < b:
        resultat = c
        return resultat
    else:
        resultat = a*b - c
        return resultat
