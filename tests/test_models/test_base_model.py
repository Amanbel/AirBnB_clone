#!/usr/bin/python3
"""unittest module"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.inst = BaseModel()

    def tearDown(self):
        pass

    def test_isBaseExist(self):
        self.assertIsNotNone(self.inst)

    def test_baseDict(self):
        self.assertIsInstance(self.inst.to_dict(), dict)

    def test_datesOfBase(self):
        Base = self.inst.to_dict()
        self.assertIsInstance(Base['created_at'], str)
        self.assertIsInstance(Base['updated_at'], str)

    def test_BaseUpdate(self):
        Base = self.inst.to_dict()
        self.inst.save()
        new_Base = self.inst.to_dict()
        self.assertNotEqual(new_Base['updated_at'], Base['updated_at'])
        self.assertEqual(new_Base['created_at'], Base['created_at'])

    def test_BaseAttributes(self):
        BaseKeys = self.inst.to_dict().keys()
        self.assertIn('id', BaseKeys)
        self.assertIn('created_at', BaseKeys)
        self.assertIn('updated_at', BaseKeys)
        self.assertIn('__class__', BaseKeys)

    def test_BaseKwargs(self):
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
