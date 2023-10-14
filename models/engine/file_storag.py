#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Class to manage the storage of instances for the Airbnb clone project."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of all objects, or objects of a specific class."""
        if cls:
            objects_dict = {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            objects_dict = self.__objects
        return objects_dict

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the objects to the JSON file."""
        objects_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Load objects from the JSON file."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                objects_dict = json.load(file)
                for k, v in objects_dict.items():
                    class_name = v['__class__']
                    if class_name in globals():
                        obj = globals()[class_name](**v)
                        key = "{}.{}".format(class_name, obj.id)
                        self.__objects[key] = obj
        except Exception:
            pass

