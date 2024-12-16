"""
Test module for sum_evens_and_odds function.

Test categories:
    - Standard cases: int numbers, float numbers, negative and mixed numbers
    - Edge cases: empty lists, single number and only even numbers
    - Defensive tests: wrong input types, assertions

Created on 2024-12-14
Author: Linah
"""

import unittest

from ..sum_evens_and_odds import sum_evens_and_odds
class TestSumEvensAndOdds(unittest.TestCase):
    """"test suite for is_in_one function"""
    def test_int_numbers(self):
        """test for all integers numbers"""
        self.assertEqual(sum_evens_and_odds([1, 2, 3, 4, 5]),{'sum_even': 6, 'sum_odd': 9})
    def test_float_numbers(self):
        """test for all float numbers"""
        self.assertEqual(sum_evens_and_odds([1.0, 2.0, 3.0]),{'sum_even': 2.0, 'sum_odd': 4.0})
    def test_int_float(self):
        """test for mixed integers and floats numbers"""
        self.assertEqual(sum_evens_and_odds([1, 3,0, 4, 5.0]),{'sum_even': 4, 'sum_odd': 9.0})
    def test_negative_numbers(self):
        """test for all negative numbers"""
        self.assertEqual(sum_evens_and_odds([-1, -2.0, -3.0]), {'sum_even': -2.0, 'sum_odd': -4.0})

# Edge Cases:
    def test_empty_list(self):
        """test for empty list should return zero"""
        self.assertEqual(sum_evens_and_odds([]), {'sum_even': 0, 'sum_odd': 0})
    def test_single_number(self):
        """test for a single element should return the single element based on type and the other type is 0"""
        self.assertEqual(sum_evens_and_odds([2.0]), {'sum_even': 2.0, 'sum_odd': 0})
    def test_all_even_number(self):
        """should return the sum of all even types and the odds sum is 0"""
        self.assertEqual(sum_evens_and_odds([2, 4, 6]), {'sum_even': 12, 'sum_odd': 0})
# Defensive Test:
    def test_numbers_not_list(self):
        """should raise an error if input is not a list"""
        with self.assertRaises(AssertionError):
            sum_evens_and_odds(12345)
    def test_not_numerical_list(self):
        """should raise an error if list items are not numbers"""
        with self.assertRaises(AssertionError):
            sum_evens_and_odds(['1', 'cat', '7.0'])
