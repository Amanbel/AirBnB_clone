#!/usr/bin/python3
import datetime

if __name__ == '__main__':
    from __init__ import storage
    from base_model import BaseModel
else:
    from models.base_model import BaseModel
    from models import storage

class User(BaseModel):
    
    def __init__(self):
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        return "[{}] ({})\
 {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        storage.new(self)
        self.update_at = datetime.datetime.now()
        storage.save()
