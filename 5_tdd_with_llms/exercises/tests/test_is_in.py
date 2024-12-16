"""
Test module for is_in function.

Test categories:
    - Standard cases: string items and two lists of string
    - Edge cases: empty lists, duplicated item, case sensitivity
    - Defensive tests: wrong input types, assertions

Created on 2024-12-14
Author: Linah
"""

import unittest

from ..is_in import is_in
class TestIsInOne(unittest.TestCase):
    """test suite for is_in function"""
    def test_item_in_one(self):
        """if item exist in only one list should return true"""
  
        self.assertEqual(is_in('o', ['o', 's'], ['y','m']), True)
    def test_item_in_both(self):
        """if item exist in both lists should return true"""
        self.assertEqual(is_in('cat',['cat', 'dog', 'lion'], ['banana', 'kiwi','cat']), True)
    def test_item_in_none(self):
        """if item does not exist in any of the lists should return false"""
        self.assertEqual(is_in('Tasabeeh',['Lina', 'Falaq', 'Rwan'],['x', 'y']), False)
#edge cases:
    def test_item_is_duplicated(self):
        """should work with duplicated items"""
        self.assertEqual(is_in('cat',['iron', 'dog', 'rat'],['cat','cat','banana']), True)
    def test_empty_lists(self):
        """test for empty list should return False"""
        self.assertEqual(is_in('cat',[],[]), False)
    def test_case_sensitivity(self):
        """test sensitivity for letter case """
        self.assertEqual(is_in('A',['a','b','c'],['b','d','f']), False)
#defensive tests:
    def test_item_is_not_string(self):
        """ should raise an error if item is not a string"""
        with self.assertRaises(AssertionError):
            is_in(123, ['t'], ['s'])
    def test_list1_is_not_list(self):
        """ should raise an error if list1 is not list"""
        with self.assertRaises(AssertionError):
            is_in('a', 'cat', ['d'])
    def test_list2_is_not_list(self):
        """ should raise an error if list2 is not list"""
        with self.assertRaises(AssertionError):
            is_in('a', ['d'], 'dog')
