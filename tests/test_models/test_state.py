#!/usr/bin/python3
""" testing stuff yeah"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ testing stuff yeah"""

    def __init__(self, *args, **kwargs):
        """ testing stuff yeah"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
