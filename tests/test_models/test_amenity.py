#!/usr/bin/python3
""" test amenity """
import os
import pep8
import models
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class TestAmenity(unittest.TestCase):
    """tedting amenity"""

    @classmethod
    def setUpClass(cls):
        """testing class"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.filestorage = FileStorage()
        cls.amenity = Amenity(name="newamenity")

        if type(models.storage) == DBStorage:
            cls.dbstorage = DBStorage()
            Base.metadata.create_all(cls.dbstorage._DBStorage__engine)
            Session = sessionmaker(bind=cls.dbstorage._DBStorage__engine)
            cls.dbstorage._DBStorage__session = Session()

    @classmethod
    def tearDownClass(cls):
        """ testing amenity """
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
        if type(models.storage) == DBStorage:
            cls.dbstorage._DBStorage__session.close()
            del cls.dbstorage

    def test_pep8(self):
        """ testing pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0, "fixing pep8")

    def test_docstrings(self):
        """Checking for docstrings."""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """Checking for attributes."""
        us = Amenity(email="a", password="a")
        self.assertEqual(str, type(us.id))
        self.assertEqual(datetime, type(us.created_at))
        self.assertEqual(datetime, type(us.updated_at))
        self.assertTrue(hasattr(us, "__tablename__"))
        self.assertTrue(hasattr(us, "name"))
        self.assertTrue(hasattr(us, "place_amenities"))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_email_not_nullable(self):
        """ testing attrib"""
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Amenity(password="a"))
            self.dbstorage._DBStorage__session.commit()
        self.dbstorage._DBStorage__session.rollback()
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Amenity(email="a"))
            self.dbstorage._DBStorage__session.commit()

    def test_is_subclass(self):
        """ testing stuff """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_two_models_are_unique(self):
        """ testing unique"""
        us = Amenity(email="a", password="a")
        self.assertNotEqual(self.amenity.id, us.id)
        self.assertLess(self.amenity.created_at, us.created_at)
        self.assertLess(self.amenity.updated_at, us.updated_at)

    def test_init_args_kwargs(self):
        """ testing kwargs"""
        dt = datetime.utcnow()
        st = Amenity("1", id="6", created_at=dt.isoformat())
        self.assertEqual(st.id, "6")
        self.assertEqual(st.created_at, dt)

    def test_str(self):
        """Test __str__ """
        s = self.amenity.__str__()
        self.assertIn("[Amenity] ({})".format(self.amenity.id), s)
        self.assertIn("'id': '{}'".format(self.amenity.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.amenity.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.amenity.updated_at)), s)
        self.assertIn("'name': '{}'".format(self.amenity.name), s)

    @unittest.skipIf(type(models.storage) == DBStorage,
                     "test DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        old = self.amenity.updated_at
        self.amenity.save()
        self.assertLess(old, self.amenity.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Amenity." + self.amenity.id, f.read())

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "test FileStorage")
    def test_save_dbstorage(self):
        """Test save method with DBStorage."""
        old = self.amenity.updated_at
        self.amenity.save()
        self.assertLess(old, self.amenity.updated_at)
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * \
                          FROM `amenities` \
                         WHERE BINARY name = '{}'".
                       format(self.amenity.name))
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(self.amenity.id, query[0][0])
        cursor.close()

    def test_to_dict(self):
        """Test dict"""
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
