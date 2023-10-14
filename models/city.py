#!/usr/bin/python3
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

