#!/usr/bin/python3
from models.base import Base
"""
this model for Rectangle class
"""


class Rectangle(Base):
    """
    The class Rectangle inherits from Base.
    Attributes:
        Private instance attributes: __width, __height, __x, __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width property"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height property"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x property"""
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        self.__x = value

    @property
    def y(self):
        """Getter for y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y property"""
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        self.__y = value
