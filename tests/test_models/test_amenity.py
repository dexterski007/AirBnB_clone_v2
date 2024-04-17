#!/usr/bin/python3
""" testing stuff yeah"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ testing stuff yeah"""

    def __init__(self, *args, **kwargs):
        """ testing stuff yeah"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
