#!/usr/bin/python3
""" testing stuff yeah"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle


class test_basemodel(unittest.TestCase):
    """ testing stuff yeah"""

    def __init__(self, *args, **kwargs):
        """ testing stuff yeah"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

        """ testing stuff yeahtest pep8 """
    def test_pep8(self):
        """ testing stuff yeahtest pycodestyle """
        pyco = pycodestyle.Styleguide(quiet=True)
        diff = pycodestyle.check_files(['models/base_model.py'])
        self.assertEqual(diff.total_errors, 0,
                         "Errors detected in pycodestyle")

    def setUp(self):
        """ testing stuff yeah"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ testing stuff yeah"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ testing stuff yeah"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ testing stuff yeah"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ testing stuff yeahTesting save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ testing stuff yeah"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ testing stuff yeah"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ testing stuff yeah"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ testing stuff yeah"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def testing_uuid(self):
        """ testing stuff yeah """
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
        """ testing stuff yeah"""
        inst6 = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst6.id, inst6.__dict__)
        self.assertEqual(string, str(inst6))


class TestFormat(unittest.TestCase):
    """ testing stuff yeah"""
    def test_pycodestylepep8(self):
        """ testing stuff yeah"""
        pycostl = pycodestyle.StyleGuide(quiet=True)
        result = pycostl.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Pycodestyle check error")


class Test_docstrings(unittest.TestCase):
    """ testing stuff yeahcheck docstrings """
    @classmethod
    def setup_class(self):
        """ testing stuff yeah"""
        self.obj_members(BaseModel, inspect.isfunction)


class TestBaseModel(unittest.TestCase):
    """ testing stuff yeahtest basemodel"""

    @classmethod
    def setUpClass(cls):
        """ testing stuff yeahsetup """
        cls.base = BaseModel()
        cls.base.name = "holb"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """ testing stuff yeah"""
        del cls.base

    def tearDown(self):
        """ testing stuff yeah"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """ testing stuff yeahtest pep8 """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_check_docstring_BaseModel(self):
        """ testing stuff yeahcheck docstrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """ testing stuff yeahcheck methods """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """ testing stuff yeahcheck if basemdel """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaseModel(self):
        """ testing stuff yeahcheck for save """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """ testing stuff yeahcheck to dict """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
