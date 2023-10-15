#!/usr/bin/python3
import json
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        Mylist = []
        for instance in list_objs:
            Mylist.append(instance.to_dictionary())  # Call to_dictionary() method
        json_list = cls.to_json_string(Mylist)
        with open("{}.json".format(cls.__name__), mode="w") as Myfile:
            Myfile.write(json_list)
