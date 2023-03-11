#!/usr/bin/python3
"""the base class of the project"""
import datetime
import uuid
from models import storage


class BaseModel():
    """base class"""

    def __init__(self, *args, **kwargs):
        """instantiates an object with the values provided"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at':
                    self.created_at = datetime.datetime.strptime(v, '%Y-%m-\
%dT%H:%M:%S.%f')
                elif k == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(v, '%Y-%m-\
%dT%H:%M:%S.%f')
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a readable string"""
        return "[{}] ({})\
 {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the update_at attribute"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns the dictionary form of the instance"""
        dict_t = self.__dict__.copy()
        dict_t.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return dict_t
