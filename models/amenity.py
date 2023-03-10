#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import datetime


if __name__ == '__main__':
    from __init__ import storage
else:
    from models import storage


class Amenity(BaseModel):
    name = ""
