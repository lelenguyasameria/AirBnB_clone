#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""

from datetime import datetime
import uuid

class BaseModel:
    """
    The BaseModel class for the AirBnB project.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The creation timestamp of the instance.
        updated_at (datetime): The last update timestamp of the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Variable-length argument list (not used).
            **kwargs: Variable-length keyword argument list.
                Each key of this dictionary is an attribute name.
                Each value of this dictionary is the value of the corresponding attribute name.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.now())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict

    def __str__(self):
        """
        Return the string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

