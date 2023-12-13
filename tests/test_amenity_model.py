#!/usr/bin/python3
"""
testing amenity model
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class test_amenity(unittest.TestCase):
    """
    Testing amenity
    """

    def test_amenity_inheritance(self):
        """
        test the amenity inherit from basemodel
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        """
        test amenity class attribute
        """
        amenity = Amenity()
        self.assertTrue("name" in amenity.__dir__())

    def test_amenity_attributes(self):
        amenity = Amenity()
        name_attr = getattr(amenity, "name")
        self.assertIsInstance(name_attr, str)
