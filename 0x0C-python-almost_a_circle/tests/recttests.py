#!/usr/bin/python3
"""test module for base"""
import os
import sys


current_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_path, '..'))
sys.path.insert(0, project_root)
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    def test_rec_id(self):
        """test rec id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(10, 7, 2, 8, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

if __name__ == '__main__':
    unittest.main()