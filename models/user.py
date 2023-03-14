#!/usr/bin/python3
import datetime
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
