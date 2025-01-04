#!/usr/bin/python3
"""This module defines a class to manage file storage
object persistence for hbnb clone
 """
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        If cls is provided, only objects of that class will be returned.
        """
        if cls is None:
            return self.__objects
        # Return only objects of specified class
        return {
            key: obj for key, obj in self.__objects.items()
            if isinstance(obj, cls)
        }

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file
        Serializes objects to the JSON file.
        """
        with open(self.__file_path, 'w') as f:
            json.dump(
                {key: obj.to_dict() for key, obj in self.__objects.items()}, f
            )

    def reload(self):
        """Loads storage dictionary from file
        Deserializes the JSON file to objects, if the file exists.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, val in data.items():
                    cls_name = key.split('.')[0]
                    cls = classes.get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it exists.
        If obj is None, this method does nothing.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
