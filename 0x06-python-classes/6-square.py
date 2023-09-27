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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square's side.
            position(tuple): is a tuple
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                any(not isinstance(v, int) or v < 0 for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

    @property
    def position(self):
        """getter for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position attribute"""
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                any(not isinstance(v, int) or v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Public instance method
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        size = self.__size
        position = self.__position

        if size == 0:
            print()
        else:
            for i in range(position[1]):
                print()
            for i in range(size):
                print(" " * position[0] + "#" * size)
