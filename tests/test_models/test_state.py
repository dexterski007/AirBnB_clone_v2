#!/usr/bin/python3
"""Testing State class"""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Testing State class"""

    def setUp(self):
        """Set up for test"""
        self.state = State()

    def tearDown(self):
        """Tear down after test"""
        del self.state

    def test_name(self):
        """Test name attribute"""
        new = self.state
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
