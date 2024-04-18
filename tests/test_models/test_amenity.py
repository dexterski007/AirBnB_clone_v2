#!/usr/bin/python3
"""Test Amenity class"""

import os
import unittest
from datetime import datetime
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from sqlalchemy.exc import OperationalError


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

        cls.filestorage = FileStorage()
        cls.amenity = Amenity(name="newamenity")

        if type(cls.filestorage) == DBStorage:
            cls.dbstorage = DBStorage()
            cls.dbstorage.reload()

    @classmethod
    def tearDownClass(cls):
        """Clean up test environment"""
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

        del cls.amenity
        del cls.filestorage

        if type(cls.filestorage) == DBStorage:
            cls.dbstorage._DBStorage__session.close()
            del cls.dbstorage

    def test_pep8(self):
        """Test PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

    def test_docstrings(self):
        """Test presence of docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """Test presence of attributes"""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))
        self.assertEqual(datetime, type(amenity.created_at))
        self.assertEqual(datetime, type(amenity.updated_at))
        self.assertTrue(hasattr(amenity, "__tablename__"))
        self.assertTrue(hasattr(amenity, "name"))

    @unittest.skipIf(type(FileStorage) == FileStorage, "Testing FileStorage")
    def test_email_not_nullable(self):
        """Test email attribute not nullable"""
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Amenity(password="a"))
            self.dbstorage._DBStorage__session.commit()

        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Amenity(email="a"))
            self.dbstorage._DBStorage__session.commit()

    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_init(self):
        """Test initialization of Amenity instance"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_two_models_are_unique(self):
        """Test uniqueness of two Amenity instances"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertLess(amenity1.created_at, amenity2.created_at)
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs"""
        dt = datetime.utcnow()
        amenity = Amenity("1", id="6", created_at=dt.isoformat())
        self.assertEqual(amenity.id, "6")
        self.assertEqual(amenity.created_at, dt)

    def test_str(self):
        """Test __str__ method"""
        string = str(self.amenity)
        self.assertIn("[Amenity] ({})".format(self.amenity.id), string)
        self.assertIn("'id': '{}'".format(self.amenity.id), string)
        self.assertIn("'created_at': {}".format(
            repr(self.amenity.created_at)), string)
        self.assertIn("'updated_at': {}".format(
            repr(self.amenity.updated_at)), string)
        self.assertIn("'name': '{}'".format(self.amenity.name), string)

    @unittest.skipIf(type(DBStorage) == DBStorage, "Test DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

        with open("file.json", "r") as f:
            self.assertIn("Amenity." + self.amenity.id, f.read())

    @unittest.skipIf(type(FileStorage) == FileStorage, "Test FileStorage")
    def test_save_dbstorage(self):
        """Test save method with DBStorage"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

        query = self.dbstorage._DBStorage__session.query(Amenity).filter(
            Amenity.name == self.amenity.name).all()
        self.assertEqual(len(query), 1)
        self.assertEqual(self.amenity.id, query[0].id)

    def test_to_dict(self):
        """Test to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(dict, type(amenity_dict))
        self.assertEqual(self.amenity.id, amenity_dict["id"])
        self.assertEqual("Amenity", amenity_dict["__class__"])
        self.assertEqual(self.amenity.created_at.isoformat(),
                         amenity_dict["created_at"])
        self.assertEqual(self.amenity.updated_at.isoformat(),
                         amenity_dict["updated_at"])
        self.assertEqual(self.amenity.name, amenity_dict["name"])


if __name__ == "__main__":
    unittest.main()
