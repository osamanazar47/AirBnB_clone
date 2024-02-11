#!/usr/bin/python3
"""
Test BaseModel:
   classes:
      
"""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
import time


class TestBaseModel(unittest.TestCase):
    """TestCases for the BaseModel class"""
    def test_instance(self):
        """test __init__"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertTrue(base.id and len(base.id) == 36
                        and base.id.count('-') == 4)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_save(self):
        base = BaseModel()
        original_updated_at = base.updated_at
        time.sleep(0.1)
        base.save()
        self.assertGreater(base.updated_at, original_updated_at)

    def test_str(self):
        """test __str__"""
        base = BaseModel()
        self.assertIsInstance(str(base), str)

    def test_to_dict(self):
        """test to_dict"""
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)
        base_dict = base.to_dict()

        # Check if '__class__' key exists and has the correct value
        self.assertIn('__class__', base_dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')

        # Check if 'id', 'created_at', and 'updated_at' keys exist
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)

        # Check if 'id' is a valid UUID
        self.assertTrue(base_dict['id'] and len(base_dict['id']) == 36 and
                        base_dict['id'].count('-') == 4)

        # Check if 'created_at' and 'updated_at' are in ISO 8601 format
        self.assertTrue(datetime.fromisoformat(base_dict['created_at']))
        self.assertTrue(datetime.fromisoformat(base_dict['updated_at']))
        # Check the typ
        self.assertIsInstance(base_dict['id'], str)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()