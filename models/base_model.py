#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""

import json
import os

class FileStorage:
    """
    The FileStorage class for the AirBnB project.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve the dictionary __objects.

        Returns:
            dict: The dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the dictionary __objects.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Save the serialized objects to the JSON file.
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """
        Load serialized objects from the JSON file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    module = __import__("models." + cls_name, fromlist=[cls_name])
                    self.__objects[key] = getattr(module, cls_name)(**value)

B
B
B
B
B
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
A
A

