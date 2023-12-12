#!/usr/bin/python3
"""
Test city model
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Testing city
    """

    def test_city_inheritance(self):
        """
        test the city inheritance from BaseModel
        """
        user_city = City()
        self.assertIsInstance(user_city, BaseModel)

    def test_city_attributes(self):
        user_city = City()
        self.assertTrue("state_id" in user_city.__dir__())
        self.assertTrue("name" in user_city.__dir__())

    def test_city_name(self):
        user_city = City()
        name = getattr(user_city, "name")
        self.assertIsInstance(name, str)

    def test_city_name(self):
        user_city = city()
        name = getattr(user_city, state_id)
        self.assertIsInstance(name, str)
