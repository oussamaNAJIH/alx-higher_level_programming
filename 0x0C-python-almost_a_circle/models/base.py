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
        if not list_dictionaries or list_dictionaries is None:
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
            Mylist.append(instance.to_dictionary())
        json_list = cls.to_json_string(Mylist)
        with open("{}.json".format(cls.__name__), mode="w") as Myfile:
            Myfile.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dict_list = json.loads(json_data)
                for item in dict_list:
                    instance = cls.create(**item)
                    instances.append(instance)
        except FileNotFoundError:
            return []
        return instances
