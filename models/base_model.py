#!/usr/bin/python3
"""the base class of the project"""
import datetime
import uuid


class BaseModel():
    """base class"""
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({})\
 {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_t = self.__dict__
        dict_t.update({'__class__': self.__class__.__name__})
        return dict_t
