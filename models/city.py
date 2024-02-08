#!/usr/bin/python3
"""Define class City"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city
    
    Attributes:
        state_id: the id of the state
        name: name of the city
    """
    state_id = ""
    name = ""