#!/usr/bin/python3
"""the base class of the project"""
import datetime
import uuid
if __name__ == 'base_model':
    from __init__ import storage
else:
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
            storage.new(self)  # adds the created object to the dictionary in FileStorage class

    def __str__(self):
        """returns a readable string"""
        return "[{}] ({})\
 {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the update_at attribute"""
        self.updated_at = datetime.datetime.now()
        storage.save() # saves the created object dictionary into a json file

    def to_dict(self):
        """returns the dictionary form of the instance"""
        dict_t = self.__dict__
        dict_t.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
            })
        return dict_t
