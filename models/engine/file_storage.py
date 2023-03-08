#!/usr/bin/python3
"""file storage module"""
import json


class FileStorage():
    """file storage class that
    serializes and deserializes JSON file"""

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        return type(self).__objects

    def new(self, obj):
        type(self).__objects.update({'{}.\
{}'.format(obj.__class__.__name__, obj.id): str(obj)})

    def save(self):
        with open(type(self).__file_path, 'w') as f:
            json.dump(type(self).__objects, f)

    def reload(self):
        try:
            with open(type(self).__file_path, 'r') as f:
                type(self).__objects.update(json.load(f))
        except FileNotFoundError:
            pass
