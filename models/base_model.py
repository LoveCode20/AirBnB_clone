#!/usr/bin/env python3
"""
Create a Base Model that defines all common attributes/methods
for the other classes
"""
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """creation of the BaseModel class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creation of a dictionary represantation"""
        instance_dict = self.__dict__.copy()
        """add __class__ key with the same class name"""
        instance_dict['__class__'] = self.__class__.__name__
        """convert the created_at and the updated_at to ISO"""
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return (instance_dict)

    def __str__(self):

        """string represantation of the instance"""
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"
