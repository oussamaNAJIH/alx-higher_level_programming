
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        n = len(row)
        for i in range(n):
            if i == n - 1:
                print("{:d}".format(row[i]))
            else:
                print("{:d} ".format(row[i]), end="")
    print()
