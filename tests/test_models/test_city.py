#!/usr/bin/python3
""" testing stuff yeah"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class test_City(test_basemodel):
    """ testing stuff yeah"""

    def __init__(self, *args, **kwargs):
        """ testing stuff yeah"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """test User"""

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_city(unittest.TestCase):
    """ testing stuff yeah"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """ testing stuff yeah"""
        del cls.city

    def tearDown(self):
        """ testing stuff yeah"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_city(self):
        """ testing stuff yeah"""
        pycostyle = pep8.StyleGuide(quiet=True)
        py = pycostyle.check_files(['models/city.py'])
        self.assertEqual(py.total_errors, 0, "pep8 errors")

    def test_check_docstring_City(self):
        """ testing stuff yeah"""
        self.assertIsNotNone(City.__doc__)

    def test_attr_City(self):
        """ testing stuff yeah"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """ testing stuff yeah"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attr_typescity(self):
        """ testing stuff yeah"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_savecity(self):
        """ testing stuff yeah"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_dictcity(self):
        """ testing stuff yeah"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()

