#!/usr/bin/python3
"""Testing BaseModel class"""

import os
import unittest
import json
import pycodestyle
import pep8
import inspect
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.base = BaseModel()
        cls.base.name = "holb"
        cls.base.num = 20

    @classmethod
    def tearDownClass(cls):
        """Clean up test environment"""
        del cls.base

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Test PEP8 compliance for BaseModel"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/base_model.py'])
        self.assertEqual(pep.total_errors, 0, "PEP8 errors found")

    def test_check_docstring_BaseModel(self):
        """Check docstrings for BaseModel"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """Check methods in BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Check if base is instance of BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    def test_save_BaseModel(self):
        """Check save method of BaseModel"""
        old_created_at = self.base.created_at
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)
        self.assertEqual(old_created_at, self.base.created_at)

    def test_to_dict_BaseModel(self):
        """Check to_dict method of BaseModel"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


class TestFormat(unittest.TestCase):
    """Test cases for code formatting"""

    def test_pycodestylepep8(self):
        """Test Pycodestyle (PEP8) compliance"""
        pycostl = pycodestyle.StyleGuide(quiet=True)
        result = pycostl.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Pycodestyle check error")


class TestDocstrings(unittest.TestCase):
    """Test cases for docstrings"""

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.obj_members(BaseModel, inspect.isfunction)

    def obj_members(self, obj, condition):
        """Check if object members have docstrings"""
        for name, data in inspect.getmembers(obj):
            if condition(data):
                self.assertIsNotNone(data.__doc__)

    def test_docstrings(self):
        """Check docstrings"""
        pass


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Set up test environment"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_pep8(self):
        """Test PEP8 compliance"""
        pyco = pep8.StyleGuide(quiet=True)
        diff = pyco.check_files(['models/base_model.py'])
        self.assertEqual(diff.total_errors, 0, "PEP8 errors found")

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """Test default values"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test initialization with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test initialization with integer kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test __str__ method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                        i.__dict__))

    def test_todict(self):
        """Test to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test initialization with None kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """Test id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def testing_uuid(self):
        """Test UUID generation"""
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
        """Test __str__ method"""
        inst6 = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst6.id, inst6.__dict__)
        self.assertEqual(string, str(inst6))


if __name__ == "__main__":
    unittest.main()
