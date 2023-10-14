#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review of a property.

    Attributes:
        place_id (str): The ID of the property being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

