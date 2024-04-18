#!/usr/bin/python3
"""Module for testing db storage"""

import os
import pep8
import inspect
import unittest
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine import db_storage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine

DBStorage = db_storage.DBStorage
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """Class to test the documentation of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that db_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test that test_db_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_engine/test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_st_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None, "db_storage.py miss docs")
        self.assertTrue(len(db_storage.__doc__) >= 1, "db_storage.py - docs")

    def test_db_st_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None, "DBStorage class miss docs")
        self.assertTrue(len(DBStorage.__doc__) >= 1, "DBStorage class - docs")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{} method missing docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{} method missing docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Class to test the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        if storage_t == 'db':
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="Los Angeles")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="New Jersey", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="alx@yahoo.com", password="passw0rd")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="Python")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Toilets")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="Nice place")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """Tear down after the test"""
        if storage_t == 'db':
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            cls.storage._DBStorage__session.close()

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_pep8(self):
        """Test that db_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_attributes(self):
        """Test DBStorage attributes"""
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_all(self):
        """Test all method"""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 6)

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_all_cls(self):
        """Test all method with a specific class"""
        obj = self.storage.all(State)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(self.state, list(obj.values())[0])

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_new(self):
        """Test new method"""
        st = State(name="New Hampshire")
        self.storage.new(st)
        store = list(self.storage._DBStorage__session.new)
        self.assertIn(st, store)

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_save(self):
        """Test save method"""
        st = State(name="Los Alamos")
        self.storage._DBStorage__session.add(st)
        self.storage.save()
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = 'Los Alamos'")
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(st.id, query[0][0])
        cursor.close()

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_delete(self):
        """Test delete method"""
        st = State(name="New Hampshire")
        self.storage._DBStorage__session.add(st)
        self.storage._DBStorage__session.commit()
        self.storage.delete(st)
        self.assertIn(st, list(self.storage._DBStorage__session.deleted))

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_delete_none(self):
        """Test delete method with None"""
        try:
            self.storage.delete(None)
        except Exception:
            self.fail

    @unittest.skipIf(storage_t != 'db', "Not using DB storage")
    def test_reload(self):
        """Test reload method"""
        og_session = self.storage._DBStorage__session
        self.storage.reload()
        self.assertIsInstance(self.storage._DBStorage__session, Session)
        self.assertNotEqual(og_session, self.storage._DBStorage__session)
        self.storage._DBStorage__session.close()
        self.storage._DBStorage__session = og_session


if __name__ == "__main__":
    unittest.main()
