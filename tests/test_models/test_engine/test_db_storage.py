#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStoragedocstringunittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """ """
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """ """
        pep8doc = pycodestyle.StyleGuide(quiet=True)
        results = pep8doc.check_files(['models/engine/db_storage.py'])
        self.assertEqual(results.total_errors, 0, "pep8 erros")

    def test_pep8_conformance_test_db_storage(self):
        """ """
        pep8doc = pycodestyle.StyleGuide(quiet=True)
        results = pep8doc.check_files(['tests/test_models/test_engine/\
                                      test_db_storage.py'])
        self.assertEqual(results.total_errors, 0, "pep8 errors")

class TestDBStorageDocs(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """ """
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """ """
        pep8doc = pycodestyle.StyleGuide(quiet=True)
        results = pep8doc.check_files(['models/engine/db_storage.py'])
        self.assertEqual(results.total_errors, 0, "pep8 errors")

    def test_pep8_conformance_test_db_storage(self):
        """ """
        pep8doc = pycodestyle.StyleGuide(quiet=True)
        results = pep8doc.check_files(['tests/test_models/test_engine/\
                                      test_db_storage.py'])
        self.assertEqual(results.total_errors, 0, "pep8 errors")

    def test_db_st_module_docstring(self):
        """ """
        self.assertIsNot(db_storage.__doc__, None, "db_storage.py miss docs")
        self.assertTrue(len(db_storage.__doc__) >= 1, "db_storage.py - docs")

    def test_db_st_class_docstring(self):
        """ """
        self.assertIsNot(DBStorage.__doc__, None, "DBStorage class miss docs")
        self.assertTrue(len(DBStorage.__doc__) >= 1, "DBStorage class - docs")

    def test_dbs_func_docstrings(self):
        """ """
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method missing docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method missing docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """ """
    @unittest.skipIf(storage_t != 'db', "skip db test")
    def test_all_returns_dict(self):
        """ """
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "skip db test")
    def test_all_no_class(self):
        """ """

    @unittest.skipIf(storage_t != 'db', "skip db test")
    def test_new(self):
        """ """

    @unittest.skipIf(storage_t != 'db', "skip db test")
    def test_save(self):
        """ """
