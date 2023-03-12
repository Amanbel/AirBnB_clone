#!/usr/bin/python3
"""file storage module"""
import json


class FileStorage():
    """file storage class that
    serializes and deserializes JSON file"""

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """returns a dictionary of all the objects with
        the key <class name>.id and a value of 
        the string return of the object
        """
        return type(self).__objects

    def new(self, obj):
        """creates a new dictionary element with the
        key as <class name>.id and the value as the
        string return of the object
        """
        type(self).__objects.update({'{}.\
{}'.format(obj.__class__.__name__, obj.id): str(obj)})

    def save(self):
        """saves the all dictionary created by the new method
        in the FileStorage class to a file,currently named
        "file.json"
        """
        with open(type(self).__file_path, 'w') as f:
            json.dump(type(self).__objects, f)

    def reload(self):
        """updates the private class attribute __object with
        the newly added attributes in the file.json file
        """
        try:
            with open(type(self).__file_path, 'r') as f:
                type(self).__objects.update(json.load(f))
        except FileNotFoundError:
            pass
