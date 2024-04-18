#!/usr/bin/python3
"""Testing Review class"""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Testing Review class"""

    def setUp(self):
        """Set up for test"""
        self.review = Review()

    def tearDown(self):
        """Tear down after test"""
        del self.review

    def test_place_id(self):
        """Test place_id attribute"""
        new = self.review
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test user_id attribute"""
        new = self.review
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test text attribute"""
        new = self.review
        self.assertEqual(type(new.text), str)


if __name__ == "__main__":
    unittest.main()
