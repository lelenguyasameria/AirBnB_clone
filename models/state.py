#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):

        self.name = ""

=======
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that inherits from BaseModel"""
    name = ""
>>>>>>> origin/BNB
