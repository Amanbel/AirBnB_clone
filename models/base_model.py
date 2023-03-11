#!/usr/bin/python3
"""the base module of the project
that enables us to create the initial
starting point of the data construction
"""

import datetime
import uuid
from models import storage


class BaseModel():
    """the base class of the project
which contain all the fundamental
attributes needed
    """

    def __init__(self, *args, **kwargs):
        """instantiates an object with the values provided
to the class or creates the values it self incase the data
isn't provided
        """
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
        """returns a readable string for users or
developers to investigate the data that has been manifested
        """
        return "[{}] ({})\
 {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the update_at attribute and saves the attributes
in this class to a private class attribute in the FileStorage module
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns the dictionary form of the instance with a tweak
in the 'created_at' and 'updated_at' attributes, and the method adds the name
of the class it came from
        """
        dict_t = self.__dict__.copy()
        dict_t.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return dict_t
