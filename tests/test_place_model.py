#!/usr/bin/python3
"""
testing place model
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Testing Place Class
    """

    def test_place_inheritance(self):
        """
        test the place class inherit from BaseModel
        """
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)

    def test_place_attributes(self):
        """
        testing place class attributes
        """
        new_place = Place()
        self.assertTrue("city_id" in new_place.__dir__())
        self.assertTrue("user_id" in new_place.__dir__())
        self.assertTrue("description" in new_place.__dir__())
        self.assertTrue("number_rooms" in new_place.__dir__())
        self.assertTrue("number_bathrooms" in new_place.__dir__())
        self.assertTrue("max_guest" in new_place.__dir__())
        self.assertTrue("price_by_night" in new_place.__dir__())
        self.assertTrue("longitude" in new_place.__dir__())
        self.assertTrue("latitude" in new_place.__dir__())
        self.assertTrue("amenity_ids" in new_place.__dir__())

    def test_type_city_id(self):
        """
        test for city_id
        """
        new_place = Place()
        city_id = getattr(new_place, "city_id")
        self.assertIsInstance(city_id, str)

    def test_type_user_id(self):
        """
        test for user_id
        """
        new_place = Place()
        user_id = getattr(new_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_description(self):
        """
        test for description
        """
        new_place = Place()
        description = getattr(new_place, "description")
        self.assertIsInstance(description, str) 

    def test_type_name(self):
        """
        test for name
        """
        new_place = Place()
        name = getattr(new_place, "name")
        self.assertIsInstance(name, str)

    def test_type_number_rooms(self):
        """
        test for number_rooms
        """
        new_place = Place()
        number_rooms = getattr(new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_number_bathrooms(self):
        """
        test for number_bathrooms
        """
        new_place = Place()
        number_bathrooms = getattr(new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_max_guest(self):
        """
        test for max_guest
        """
        new_place = Place()
        max_guest = getattr(new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_price_by_night(self):
        """
        test for price_by_night
        """
        new_place = Place()
        price_by_night = getattr(new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_longitude(self):
        """
        test for longitude
        """
        new_place = Place()
        longitude = getattr(new_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        """
        test for latitude
        """
        new_place = Place()
        latitude = getattr(new_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_amenity(self):
        """
        test for amenity_ids
        """
        new_place = Place()
        amenity = getattr(new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)
