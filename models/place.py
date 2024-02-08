#!/usr/bin/python3
"""Define class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place

    Attributes:
        city_id(str): the name and id of the city
        user_id(str): the name and id of the user
        name(str): the name of the place
        description(str): a description of the place
        number_rooms(int): the number of rooms in the place
        number_bathrooms(int): the number of bathrooms in the place
        max_quest(int): the max number of quests allowed
        price_by_night(int): the price by night
        latitude(float): the latitude
        longitude(float): the longitude
        amenity_ids(list): the list of the amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
