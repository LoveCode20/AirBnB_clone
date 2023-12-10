#!/usr/bin/env python3
"""creation of the FileStorage class"""
import json
from os import path
import models
from os.path import exists


class FileStorage:
    """serializes instance to a Json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with the <obj class>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the json file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding='utf-8')as file:
                json.dump(obj_dict, file)

    def reload(self):
        """deserializes the Json file to __objects"""
        if exists(FileStorage.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel

                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = (
                        BaseModel(**value if class_name == 'BaseModel' else None)
                            )
                if obj_instance:
                    self.__objects[key] = obj_instance


storage = FileStorage()
storage.reload()
