#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city where properties are located.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state where the city is located.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
        self.state_id = ""

=======
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that inherits from BaseModel"""
    state_id = ""
    name = ""
>>>>>>> origin/BNB
