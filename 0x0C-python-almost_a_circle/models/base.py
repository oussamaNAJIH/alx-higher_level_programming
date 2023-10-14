#!/usr/bin/python3
"""
this model for base class
"""


class Base:
    """
    Base class for managing id attribute.
    Attributes:
        __nb_objects (int): Private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        Args:
            id (int): An optional integer identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
