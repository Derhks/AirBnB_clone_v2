#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic_cls = {}
        if cls:
            for key, value in self.__objects.items():
                if cls == type(value):
                    dic_cls[key] = value
            return dic_cls
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """This function loads every dictionary representation of the object"""
        Class_type = {'BaseModel': BaseModel, 'User': User,
                      'State': State}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                Loaded_file = load(f)
                for key in Loaded_file.keys():
                    for Class, instance in Class_type.items():
                        if Loaded_file[key]['__class__'] == Class:
                            FileStorage.__objects[key] = (
                                (instance)(**Loaded_file[key]))
        except:
            pass

    def delete(self, obj=None):
        """delete the object if exists"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
        else:
            pass

    def close(self):
        """This method call to the method reload"""
        self.reload()
