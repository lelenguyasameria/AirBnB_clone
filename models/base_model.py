<<<<<<< HEAD
#!/usr/bin/python3
"""Defines base model classes for the Airbnb clone project."""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base model class for all project classes."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    
    def __init__(self, *args, **kwargs):
        
        self.name = ""

class Review(BaseModel):
    """Represents a review of a property.

    Attributes:
        place_id (str): The ID of the property being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    def __init__(self, *args, **kwargs):
    
        self.place_id = ""
        self.user_id = ""
        self.text = ""

class Place(BaseModel):
    """Represents a property (place) available for rent.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night for renting the place.
        latitude (float): The latitude coordinate of the place's location.
        longitude (float): The longitude coordinate of the place's location.
        amenity_ids (list): A list of Amenity IDs associated with the place.
    """

    def __init__(self, *args, **kwargs):
        
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

class City(BaseModel):
    """Represents a city where properties are located.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state where the city is located.
    """

    def __init__(self, *args, **kwargs):
    
        self.name = ""
        self.state_id = ""

class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):

        self.name = ""

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
#!/usr/bin/env python3
"""
BaseModel that defines all common attributes/methods for other classes
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes the data"""
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if "__class__" not in key:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print string representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['created_at'] = self.created_at.isoformat()
        return dictionary
>>>>>>> origin/BNB
