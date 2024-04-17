#!/usr/bin/python3
""" testing stuff yeah"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ testing stuff yeah"""

    def __init__(self, *args, **kwargs):
        """ testing stuff yeah"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
