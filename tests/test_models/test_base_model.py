#!/usr/bin/python3
"""unittest module"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """test class for BaseModel class
    to test its methods"""

    def setUp(self):
        """function called before every test
        function"""
        self.inst = BaseModel()

    def tearDown(self):
        """function called after every test
        function"""
        pass

    def test_isBaseExist(self):
        """function to test the initialization of
        the BaseClass"""
        self.assertIsNotNone(self.inst)

    def test_baseDict(self):
        """function to test the to_dict()
        method inside the BaseClass the
        returns the dictionary of the object"""
        self.assertIsInstance(self.inst.to_dict(), dict)

    def test_datesOfBase(self):
        """function that tests the type of the
        value of the created_at and updated_at values"""
        Base = self.inst.to_dict()
        self.assertIsInstance(Base['created_at'], str)
        self.assertIsInstance(Base['updated_at'], str)

    def test_BaseUpdate(self):
        """function that tests the save() method if
        it updated the updated_at attribute"""
        Base = self.inst.to_dict()
        self.inst.save()
        new_Base = self.inst.to_dict()
        self.assertNotEqual(new_Base['updated_at'], Base['updated_at'])
        self.assertEqual(new_Base['created_at'], Base['created_at'])

    def test_BaseAttributes(self):
        """funciton that tests the creation of
        the fundamental attributes in the BaseClass"""
        BaseKeys = self.inst.to_dict().keys()
        self.assertIn('id', BaseKeys)
        self.assertIn('created_at', BaseKeys)
        self.assertIn('updated_at', BaseKeys)
        self.assertIn('__class__', BaseKeys)

    def test_BaseKwargs(self):
        """function that tests the initialization of
        BaseClass with a dictionary input"""
        Base_dict = self.inst.to_dict()
        Base_dict.update({'name': "Aman", 'age': 54, '__class__': 'User'})
        Base = BaseModel(**Base_dict)
        Base_new = Base.to_dict()
        new_Base_keys = Base.to_dict().keys()
        self.assertIsInstance(Base.created_at, datetime.datetime)
        self.assertIsInstance(Base.updated_at, datetime.datetime)
        self.assertIn('name', new_Base_keys)
        self.assertIn('age', new_Base_keys)
        self.assertNotEqual(Base_dict['__class__'], Base_new['__class__'])


if __name__ == "__main__":
    unittest.main()
