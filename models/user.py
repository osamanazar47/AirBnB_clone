#!/usr/bin/python3
"""a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Define a User class
    email: string
    password: string
    first_name: string
    last_name: string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
