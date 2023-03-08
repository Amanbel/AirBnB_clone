#!/usr/bin/python3
"""the base class of the project"""
import datetime
import uuid


class BaseModel():
    """base class"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for k,v in kwargs.items():
                if k == 'created_at':
                    self.created_at = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({})\
 {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_t = self.__dict__
        dict_t.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
            })
        return dict_t
