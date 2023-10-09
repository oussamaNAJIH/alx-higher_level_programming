#!/usr/bin/python3
"""
module that uses base_geometry modules
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializes objects
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
