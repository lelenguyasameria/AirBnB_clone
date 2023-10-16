#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user of the Airbnb clone platform.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

=======
"""Class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
>>>>>>> origin/BNB
