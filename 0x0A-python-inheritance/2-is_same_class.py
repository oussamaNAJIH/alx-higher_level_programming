#!/usr/bin/python3
"""
checjing if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an
    instance of the specified class ; otherwise False
    """
    return type(obj) is a_class
