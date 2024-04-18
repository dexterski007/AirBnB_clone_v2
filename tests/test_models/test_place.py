#!/usr/bin/python3
""" Testing Place class """

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """ Testing Place class """

    def setUp(self):
        """ Set up for test """
        self.place = Place()

    def tearDown(self):
        """ Tear down after test """
        del self.place

    def test_city_id(self):
        """ Test city_id attribute """
        new = self.place
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test user_id attribute """
        new = self.place
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test name attribute """
        new = self.place
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test description attribute """
        new = self.place
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test number_rooms attribute """
        new = self.place
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test number_bathrooms attribute """
        new = self.place
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test max_guest attribute """
        new = self.place
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test price_by_night attribute """
        new = self.place
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test latitude attribute """
        new = self.place
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test longitude attribute """
        new = self.place
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ Test amenity_ids attribute """
        new = self.place
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
