#!/usr/bin/python3
"""this module defines a class Square
    classes :
        Square: A class to create and manipulate square objects
"""


class Square:
    """class Square that allows to create objects or squares
        methodes:
            init: used to initialize instances
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
