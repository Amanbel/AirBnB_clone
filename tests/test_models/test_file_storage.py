#!/usr/bin/python3
"""FileStorage class unittest module
, that tests the methods and functionality of 
the class"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.inst = FileStorage()

    def test_FileStorageSave(self):
        self.inst.save()
        self.assertTrue(os.path.isfile('./file.json'))

    def test_FileStorageNew(self):
        Base = BaseModel()
        self.inst.new(Base)
        self.inst.save()
        with open('file.json', 'r') as f:
            d = json.load(f)
        objs_str = d.values()
        self.assertIn(str(Base), objs_str)

    def test_FileStorageAll(self):
        Base1 = BaseModel()
        Base2 = BaseModel()
        Base3 = BaseModel()
        list_objs = [Base1, Base2, Base3]
        for o in list_objs:
            self.inst.new(o)
        all_dict = self.inst.all().values()
        for o in list_objs:
            self.assertIn(str(o), all_dict)

    def test_FileStorageReload(self):
        Base = BaseModel()
        B_todict = Base.to_dict()
        B_todict.update({'id': 2424})
        Base_new = BaseModel(**B_todict)
        key = "{}.{}".format(type(Base_new).__name__, Base_new.id)
        input_dict = self.inst.all()
        input_dict.update({key: str(Base_new)})
        with open('file.json', 'w') as f:
            json.dump(input_dict, f)
        self.inst.reload()
        all_dict = self.inst.all().values()
        self.assertIn(str(Base_new), all_dict)
