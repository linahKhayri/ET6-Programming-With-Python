"""
Test module for sort_numbers function.

Test categories:
    - Standard cases: int or float or both list
    - Edge cases: empty lists, single item, identical items, sorted list
    - Defensive tests: wrong input types, assertions

Created on 2024-12-14
Author: Linah
"""
import unittest
from ..sort_numbers import sort_numbers

class TestSortNumbers(unittest.TestCase):

# Standard cases
    def test_int(self):
        """should deal with int and return sorted list of int"""
        self.assertEqual(sort_numbers([4, 3, 1, 2]), [1, 2, 3, 4])

    
    def test_float(self):
        """should deal with float and return sorted list of float"""
        self.assertEqual(sort_numbers([9.0, 7.0, 5.0]), [5.0, 7.0, 9.0])
        
    def test_mixed_list(self):
        """should return a mixed sorted list"""
        self.assertEqual(sort_numbers([9.0, 8, 6.0, 0]),[0, 6.0, 8, 9.0])

    def test_positive_list(self):
        """test for positive list"""
        self.assertEqual(sort_numbers([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])

    def test_negative_list(self):
        """test for negative list"""
        self.assertEqual(sort_numbers([-4, -1, -2.0, -3]), [-4, -3, -2.0, -1])

# Edge cases
    def test_empty_list(self):
        """return empty list"""
        self.assertEqual(sort_numbers([]), [])

    def test_single_item(self):
        """return the same item"""
        self.assertEqual(sort_numbers([7]), [7])  # Fixed this line

    def test_identical_items(self):
        """return the same list"""
        self.assertEqual(sort_numbers([99, 99, 99]), [99, 99, 99])

    def test_sorted_list(self):
        """return the same sorted list"""
        self.assertEqual(sort_numbers([1, 2, 3]), [1, 2, 3])

# Defensive tests
    def test_is_not_list(self):
        """should raise an AssertionError if input is not a list"""
        with self.assertRaises(AssertionError):
            sort_numbers('meow')  # String instead of list

    def test_items_are_not_numbers(self):
        """should raise an AssertionError if list items are not numbers"""
        with self.assertRaises(AssertionError):
            sort_numbers(['cat', '7', 'd'])  # Non-numeric values in the list
