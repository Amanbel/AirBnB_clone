#!/usr/bin/python3
"""FileStorage class unittest module
, that tests the methods and functionality of
the class"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.engine import file_storage


class TestFileStorage(unittest.TestCase):
    """test class for the file_storage module
    , tests the metthods and functionality of the
    FileStorage class inside the file_storage module
    """

    def setUp(self):
        """the initial function that is called
        before every test is called"""
        self.inst = FileStorage()

    def tearDown(self):
        """runs after every test is called"""
        pass

    def test_FileStorageSave(self):
        """tests the save() method inside the
        FileStorage class, to see if it can save the
        elements inside the __objects attribute in
        file.json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile('./file.json'))

    def test_FileStorageNew(self):
        """tests the new() method to see if it
        saves the instance of the object passed to
        the method inside the __objects attribute
        in the form of <class name>.id as key and
        the string return of the object as value"""
        Base = BaseModel()
        self.inst.new(Base)
        self.inst.save()
        with open('file.json', 'r') as f:
            d = json.load(f)
        objs_str = d.values()
        self.assertIn(str(Base), objs_str)

    def test_FileStorageAll(self):
        """tests the all() method in the FileStorage
        class to retrive all the elements from the
        __objects attribute"""
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
        """tests the reload() method inside the
        FileStorage class, to see if it can
        retrive all the elements from the file.json
        file and store it in __objects attribute"""
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

if __name__ == "__main__":
    unittest.main()
