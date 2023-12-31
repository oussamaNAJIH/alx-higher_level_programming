#!/usr/bin/python3
"""
this module for inheriting from list
"""


class MyList(list):
    """
    this class inherits from list class
    """
    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
