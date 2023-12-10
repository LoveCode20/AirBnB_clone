#!/usr/bin/python3
"""
creation of the class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """implementation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
