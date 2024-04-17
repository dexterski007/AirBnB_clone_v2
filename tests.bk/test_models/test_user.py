#!/usr/bin/python3
""" testing stuff yeah"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ testing stuff yeah"""

    def __init__(self, *args, **kwargs):
        """ testing stuff yeah"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
