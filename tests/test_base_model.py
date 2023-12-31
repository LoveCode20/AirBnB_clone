#!/usr/bin/env python3
"""
creation of a unittest for the base class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBasemodel(unittest.TestCase):
    """creation of tester"""
    def test_init(self):
        """function which tests the constructor of the basemodel"""
        a = BaseModel()
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.updated_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)

    def test_str_(self):
        """method that tests for the string returned in basemodel"""
        b = BaseModel()
        exp = f"[BaseModel] ({b.id}) {b.__dict__}"
        self.assertEqual(str(b), exp)


if __name__ == "__main__":
    unittest.main()
