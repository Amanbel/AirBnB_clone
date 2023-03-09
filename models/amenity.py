#!/usr/bin/python3
from base_model import BaseModel
import datetime


if __name__ == '__main__':
    from __init__ import storage
else:
    from models import storage


class Amenity(BaseModel):
    name = ""

    def __init__(self):
        super().__init__()

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def __str__(self):
        """returns a readable string"""
        return "[{}] ({})\
 {}".format(self.__class__.__name__, self.id, self.__dict__)

if __name__ == '__main__':
    # testing the class if it works as excpected
    am = Amenity()
    print(str(am))
    am.name = "hilton"
    am.save()
    print(str(am))
