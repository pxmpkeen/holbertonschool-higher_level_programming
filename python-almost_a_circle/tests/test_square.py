"""Tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """Class to test Square class"""
    def test_getter(self):
        r1 = Square(2)
        self.assertEqual(r1.size, 2)

    def test_setter(self):
        r1 = Square(12)
        r1.size = 13
        self.assertEqual(r1.size, 13)

    def test_string(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = "Dude"

    def test_negative(self):
        r1 = Square(3)

        with self.assertRaises(ValueError):
            r1.size = -43

    def test_zero(self):
        r1 = Square(3)

        with self.assertRaises(ValueError):
            r1.size = 0

    def test_decimal(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = 1.5

    def test_tuple(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = (1, 1)

    def test_empty(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = ''

    def test_none(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = None

    def test_list(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = [1, 2]

    def test_dict(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = {"Dude": 5, "Nigga": 8}

    def test_width(self):
        r1 = Square(5)
        r1.size = 6
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0

        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected)

        s1 = Square(1, 0, 0, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s1_dictionary, expected)

        s1.update(5, 5, 5, 5)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        self.assertEqual(s1_dictionary, expected)
