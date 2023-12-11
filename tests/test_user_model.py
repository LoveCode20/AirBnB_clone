#!/usr/bin/python3
"""
Test for user model
"""

import sys
import datetime
import unittest
from io import StringIO
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test for user class
    """

    def Test_User_inheritance(self):
        """
        test if the user class inherits from BaseModel
        """

        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        """
        Test for user class attributes
        """

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_type_first_email(self):
        """
        test the type of email
        """
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        """
        test the type of first_name
        """
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        """
        test the type of last_name
        """
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        """
        test the type of password
        """
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)
