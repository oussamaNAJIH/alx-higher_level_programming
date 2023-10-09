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
        self.sort()
        print(self)

