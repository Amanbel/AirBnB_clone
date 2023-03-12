#!/usr/bin/python3
"""Test suite for the User class of the models.user module"""
import unittest

from models.base_model import BaseModel
from models.user import User


class TestState(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        self.user = User()

    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_class_attrs(self):
        self.assertIs(type(self.user.email), str)
        self.assertFalse(bool(self.user.email))
        self.assertIs(type(self.user.password), str)
        self.assertFalse(bool(self.user.password))
        self.assertIs(type(self.user.first_name), str)
        self.assertFalse(bool(self.user.first_name))
        self.assertIs(type(self.user.last_name), str)
        self.assertFalse(bool(self.user.last_name))
