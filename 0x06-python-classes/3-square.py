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

    def area(self):
        """
        Public instance method
        returns the current square area
        """
        return self.__size ** 2
