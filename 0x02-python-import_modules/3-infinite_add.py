#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arguments = len(sys.argv) - 1
    sum = 0
    if num_arguments == 0 or num_arguments == 1:
        print("{}".format(num_arguments))
    else:
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])

        print("{}".format(sum))
