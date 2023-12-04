#!/usr/bin/env python3
"""creation of the FileStorage class"""
import json
from os.path import exists


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    FileStorage.__objects[key] = obj
