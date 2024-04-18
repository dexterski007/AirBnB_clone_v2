#!/usr/bin/python3
"""Testing City class"""

import os
import unittest
import pycodestyle
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Testing City class"""

    def setUp(self):
        """Set up for test"""
        self.city = City()
        self.city.name = "LA"
        self.city.state_id = "CA"

    def tearDown(self):
        """Tear down after test"""
        del self.city
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_city(self):
        """Test PEP8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors")

    def test_check_docstring_City(self):
        """Test if City class has docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_city_attributes(self):
        """Test City class attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attribute_types(self):
        """Test types of City class attributes"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save_method(self):
        """Test save method of City"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of City"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)


if __name__ == "__main__":
    unittest.main()
