#!/usr/bin/python3
from models.rectangle import Rectangle
"""
This model for square class
"""


class Square(Rectangle):
    """
    Class Square inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
