#!/usr/bin/env python3
"""
Create a Base Model that defines all common attributes/methods
for the other classes
"""
import models
import uuid
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
    """creation of the BaseModel class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    """convert string represantation ot datetime object"""
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """Add the instance to storage if it's new instance"""
            storage.new(self)

    def save(self):
        """save the instance and call save() method of storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creation of a dictionary represantation"""
        obj_dict = self.__dict__.copy()
        """add __class__ key with the same class name"""
        obj_dict['__class__'] = self.__class__.__name__
        """
        convert the created_at and the updated_at to ISO to ease the transfer
        """
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """string represantatino of the instance"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")
