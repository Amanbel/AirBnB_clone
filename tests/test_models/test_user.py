#!/usr/bin/python3
"""the unittest module for the User class
that tests the attributes and inherited attributes
of the BaseModel"""
import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """class used to test the User class
    , the class inherits from unittest"""

    def setUp(self):
        """the first function that gets called
        before evert test function"""
        self.inst = User()

    def tearDown(self):
        """the last function that gets called
        after every function"""
        pass

    def test_UserExist(self):
        """function that tests the existance of
        the instance of the User class"""
        self.assertIsNotNone(self.inst)

    def test_UserClassName(self):
        """function that tests the name of the instance
        that was created by the User class"""
        user_attr = self.inst.to_dict()
        self.assertEqual('User', user_attr['__class__'])

    def test_UserAttributes(self):
        """function that tests the funcdamental attributes
        of the User class instance"""
        user_attr = self.inst.to_dict().keys()
        self.assertIn('id', user_attr)
        self.assertIn('created_at', user_attr)
        self.assertIn('updated_at', user_attr)
        self.assertEqual(type(self.inst).__name__, 'User')

    def test_UserDatetime(self):
        """function that checks the type of the updated_at
        and created_at attribute, if its datetime object"""
        update_time = self.inst.updated_at
        create_time = self.inst.created_at
        self.assertIsInstance(update_time, datetime.datetime)
        self.assertIsInstance(create_time, datetime.datetime)

    def test_UserNewAttributes(self):
        """function that tests the newly added attributes
        in the instance, checks to see if they exist"""
        self.inst.first_name = 'conor'
        self.inst.last_name = 'mac gragor'
        user_attr = self.inst.to_dict()
        user_keys = user_attr.keys()
        user_values = user_attr.values()
        self.assertIn('first_name', user_keys)
        self.assertIn('last_name', user_keys)
        self.assertIn('conor', user_values)
        self.assertIn('mac gragor', user_values)

    def test_UserClassAttributes(self):
        """function that tests the class attributes available
        in the User class"""
        type(self.inst).email = 'aman@gmail.com'
        type(self.inst).password = 'root'
        type(self.inst).first_name = 'aman'
        type(self.inst).last_name = 'bel'
        user = User()
        self.assertEqual('aman@gmail.com', user.email)
        self.assertEqual('root', user.password)
        self.assertEqual('aman', user.first_name)
        self.assertEqual('bel', user.last_name)
