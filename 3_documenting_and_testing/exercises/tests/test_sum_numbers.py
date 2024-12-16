import unittest

from ..sum_numbers import sum_numbers

class Testsumnumbers(unittest.TestCase):
    """ """

    def test_int_int(self):
        """give an int sum result"""
        self.assertEqual(sum_numbers(0, 0), 0)
    def test_int_float(self):
        """ give a float sum result"""
        self.assertEqual(sum_numbers(3, 4.0), 7.0)
    def test_float_float(self):
        """give a float sum result"""
        self.assertEqual(sum_numbers(2.0, 3.0),5.0)
#edge tests: 
    def test_positive_negative(self):
        self.assertEqual(sum_numbers(1, -3.0),-2.0)
    def test_negative_negative(self):
        self.assertEqual(sum_numbers(-1,-2),-3)
#defensive tests:
    def test_None_None(self):
        with self.assertRaises(AssertionError):
            sum_numbers(None,None)
    def test_str_str(self):
        with self.assertRaises(AssertionError):
            sum_numbers(str,str)
    def test_str_first(self):
        with self.assertRaises(AssertionError):
            sum_numbers(str,(int,float))
