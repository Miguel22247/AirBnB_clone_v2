#!/usr/bin/python3
""" Module for testing db storage """
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from os import getenv
import MySQLdb
import pep8


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_db_storage(unittest.TestCase):
    """Tests the database storage"""
    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run if storage is file")
    def test_attributes_DBStorage(self):
        """Tests for class attributes"""
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'reload'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run if storage is file")
    def test_new_DBStorage(self):
        """Tests for new() method"""
        nb = self.cursor.execute("SELECT COUNT(*) FROM states")
        state = State(name="Oregon")
        state.save()
        nb1 = self.cursor.execute("SELECT COUNT(*) FROM states")
        self.assertEqual(nb1 - nb, 0)

    def test_all_DBStorage(self):
        """Tests for the all method"""
        state = State(name="California")
        storage.new(state)
        storage.save()
        key = '{}.{}'.format(type(state).__name__, state.id)
        dic = storage.all(State)
        self.assertTrue(key in dic.keys())
        state1 = State(name="Oregon")
        storage.new(state1)
        storage.save()
        key1 = '{}.{}'.format(type(state1).__name__, state1.id)
        dic1 = storage.all()
        self.assertTrue(key in dic1.keys())
        self.assertTrue(key1 in dic1.keys())
        u = User(email="scoot@noot", password="scootnoot")
        storage.new(u)
        storage.save()
        key2 = '{}.{}'.format(type(u).__name__, u.id)
        dic2 = storage.all(User)
        self.assertTrue(key2 in dic2.keys())
        self.assertFalse(key1 in dic2.keys())
        self.assertFalse(key in dic2.keys())
        self.assertFalse(key2 in dic.keys())
