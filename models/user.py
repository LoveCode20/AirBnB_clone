#!/usr/bin/python3
"""
user class module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class that provides users information
    """
    email = " "
    password = " "
    first_name = " "
    last_name = " "
