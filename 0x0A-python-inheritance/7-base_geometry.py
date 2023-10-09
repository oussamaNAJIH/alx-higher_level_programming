#!/usr/bin/python3
"""
empty module
"""


class BaseGeometry:
    """
    empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
