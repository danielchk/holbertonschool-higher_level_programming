#!/usr/bin/python3
""" Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """define unittest"""

    def test_int(self):
        self.assertEqual(max_integer([4, 6, 8, 10]), 10)
    
    def test_neg(self):
        self.assertEqual(max_integer([-4, -6, -8, -10]), -4)

    def test_var(self):
        i = 6
        self.assertEqual(max_integer([i]), i)

    def test_multiplevar(self):
        i = 6
        j = 8
        self.assertEqual(max_integer([i, j]), j)

    def test_bignumber(self):
        self.assertEqual(max_integer([3122618273182319, 664527213123, 12345678910111213]), 12345678910111213)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_zeroarg(self):
        self.assertIsNone(max_integer())

    def  test_string(self):
        self.assertEqual(max_integer("abcdefghijklmnopqrstu"), 'u')

    def test_stringerror(self):
        with self.assertRaises(TypeError):
            max_integer(["holberton", 2, 4, 6])

    def test_twolists(self):
        with self.assertRaises(TypeError):
            max_integer([2, 4, 6], [8, 10])
