#!/usr/bin/python3
""" Module for testing db storage"""
import pep8
import models
import MySQLdb
import unittest
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


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


class TestDBStoragewithmsql(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """ """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="Los_angeles")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="new_jersey", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="alx@yahoo.com", password="passw0rd")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="python")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="toilets")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="noice")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """ """
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            del cls.state
            del cls.city
            del cls.user
            del cls.place
            del cls.amenity
            del cls.review
            cls.storage._DBStorage__session.close()
            del cls.storage

    def test_pep8(self):
        """ """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """ """
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_attributes(self):
        """ """
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    def test_methods(self):
        """ """
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_init(self):
        """ """
        self.assertTrue(isinstance(self.storage, DBStorage))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_all(self):
        """ """
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 6)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_all_cls(self):
        """ """
        obj = self.storage.all(State)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(self.state, list(obj.values())[0])

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_new(self):
        """ """
        st = State(name="new_hampshite")
        self.storage.new(st)
        store = list(self.storage._DBStorage__session.new)
        self.assertIn(st, store)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_save(self):
        """ test save"""
        st = State(name="losalamos")
        self.storage._DBStorage__session.add(st)
        self.storage.save()
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = 'losalamos'")
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(st.id, query[0][0])
        cursor.close()

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_delete(self):
        """  """
        st = State(name="new_hampshite")
        self.storage._DBStorage__session.add(st)
        self.storage._DBStorage__session.commit()
        self.storage.delete(st)
        self.assertIn(st, list(self.storage._DBStorage__session.deleted))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_delete_none(self):
        """ """
        try:
            self.storage.delete(None)
        except Exception:
            self.fail

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "json test")
    def test_reload(self):
        """Test reload method."""
        og_session = self.storage._DBStorage__session
        self.storage.reload()
        self.assertIsInstance(self.storage._DBStorage__session, Session)
        self.assertNotEqual(og_session, self.storage._DBStorage__session)
        self.storage._DBStorage__session.close()
        self.storage._DBStorage__session = og_session


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

if __name__ == "__main__":
    unittest.main()
