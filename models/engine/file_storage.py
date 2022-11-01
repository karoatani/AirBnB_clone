#!/usr/bin/python3
import json
import os


class FileStorage(object):
    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict = {}
            for k, v in FileStorage.__objects.items():
                dict[k] = v.to_dict()
            json.dump(dict, f, indent=4)

    def reload(self):
        """Reloads the stored objects"""
        from models.base_model import BaseModel
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        for key, value in obj_dict.items():
            class_nam = key.split(".")[0]
            FileStorage.__objects[key] = eval(class_nam)(**value)
