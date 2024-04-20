#!/usr/bin/python3
"""Testing User class"""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """Testing User class"""

    def setUp(self):
        """Set up for test"""
        self.user = User()

    def tearDown(self):
        """Tear down after test"""
        del self.user

    def test_first_name(self):
        """Test first_name attribute"""
        new = self.user
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last_name attribute"""
        new = self.user
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test email attribute"""
        new = self.user
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test password attribute"""
        new = self.user
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
