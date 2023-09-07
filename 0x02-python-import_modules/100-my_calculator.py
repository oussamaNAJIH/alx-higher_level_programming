#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(sys.argv) == 4:
        a = sys.argv[1]
        operator = sys.argv[2]
        b = sys.argv[3]
        if operator == "+":
            resultat = add(int(a), int(b))
            print("{} + {} = {}".format(a, b, resultat))
            exit(0)
        elif operator == "-":
            resultat = sub(int(a), int(b))
            print("{} - {} = {}".format(a, b, resultat))
            exit(0)
        elif operator == "*":
            resultat = mul(int(a), int(b))
            print("{} * {} = {}".format(a, b, resultat))
            exit(0)
        elif operator == "/":
            resultat = add(int(a), int(b))
            print("{} / {} = {}".format(a, b, resultat))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
