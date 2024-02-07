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
        """add object to dictionary __objects attributes:
            obj: instance of a class
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        with the path stored in __file_path"""
        dictionary = {}
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary, f)

    def reload(self):
        """store objects from json file to __objects dictionary"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dictionary = json.load(f)
                d = {}
                for k, v in dictionary.items():
                    class_name = v['__class__']
                    print(class_name)
                    obj = globals()[class_name]
                    obj_ins = obj(**v)
                    FileStorage.__objects[k] = obj_ins
        except FileNotFoundError:
            pass
