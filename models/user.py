#!/usr/bin/python3
import datetime

if __name__ == '__main__':
    from __init__ import storage
    from base_model import BaseModel
else:
    from models.base_model import BaseModel
    from models import storage

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
