#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

        """ test pep8 """
    def test_pep8(self):
        """ test pycodestyle """
        pyco = pycodestyle.Styleguide(quiet=True)
        diff = pycodestyle.check_files(['models/base_model.py'])
        self.assertEqual(diff.total_errors, 0,
                         "Errors detected in pycodestyle")

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def testing_uuid(self):
        """  """
        inst1 = BaseModel()
        inst2 = BaseModel()
        inst3 = BaseModel()
        inst_list = [inst1, inst2, inst3]
        for instance in inst_list:
            ins_uuid = instance.id
            with self.subTest(uuid=ins_uuid):
                self.assertIs(type(ins_uuid), str)
        self.assertNotEqual(inst1.id, inst2.id)
        self.assertNotEqual(inst1.id, inst3.id)
        self.assertNotEqual(inst2.id, inst3.id)

    def test_string_method(self):
        """ """
        inst6 = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst6.id, inst6.__dict__)
        self.assertEqual(string, str(inst6))


class TestFormat(unittest.TestCase):
    """ """
    def test_pycodestylepep8(self):
        """ """
        pycostl = pycodestyle.StyleGuide(quiet=True)
        result = pycostl.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Pycodestyle check error")


class Test_docstrings(unittest.TestCase):
    """ check docstrings """
    @classmethod
    def setup_class(self):
        """ """
        self.obj_members(BaseModel, inspect.isfunction)


class TestBaseModel(unittest.TestCase):
    """ test basemodel"""

    @classmethod
    def setUpClass(cls):
        """ setup """
        cls.base = BaseModel()
        cls.base.name = "holb"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """ """
        del cls.base

    def tearDown(self):
        """ """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_check_docstring_BaseModel(self):
        """ check docstrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """ check methods """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """ check if basemdel """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaseModel(self):
        """ check for save """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """ check to dict """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
