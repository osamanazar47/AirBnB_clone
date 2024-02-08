#!/usr/bin/python3
"""Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define a review class
    place_id: string
    user_id: string
    text: string"""
    place_id = ""
    user_id = ""
    text = ""
