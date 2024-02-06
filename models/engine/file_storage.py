#!/usr/bin/python3
"""file_storage module
    dictionary <--> json file"""
import json


class FileStorage:
    """class: FileStorage
    private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - store all objects by
        <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add object to dictionary __objects
        attributes:
            obj: instance of a class
        """
        d = obj.to_dict()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = d

    def save(self):
        """serializes __objects to the JSON file
        with the path stored in __file_path"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """store objects from json file to __objects dictionary"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects.update(json.load(f))
        except FileNotFoundError:
            pass
