#!/usr/bin/python3
"""this module defines a class Square
    classes :
        Square: A class to create and manipulate square objects
"""


class Square:
    """class Square that allows to create objects or squares
        methodes:
            init: used to initialize instances
            area: returns the current square area
        attributes:
            __size: Private instance attribute
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square's side.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """getter for size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        n = self.__size
        if n == 0:
            print()
        for i in range(n):
            for j in range(n):
                if j == n - 1:
                    print("#")
                else:
                    print("#", end="")
