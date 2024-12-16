"""
Test module for is_in_one function.

Test categories:
    - Standard cases: string items and two lists of string
    - Edge cases: empty lists, duplicated item, case sensitivity
    - Defensive tests: wrong input types, assertions

Created on 2024-12-14
Author: Linah
"""

import unittest

from ..is_in_one import is_in_one
class TestIsInOne(unittest.TestCase):
    """test suite for is_in_one function"""
    def test_item_in_one(self):
        """if item exist in only one list should return true"""

        self.assertEqual(is_in_one('o', ['o', 's'], ['y','m']), True)
    def test_item_in_both(self):
        """if item exist in both lists should return False"""
        self.assertEqual(is_in_one('cat',['cat', 'dog', 'lion'], ['banana', 'kiwi','cat']), False)
    def test_item_in_none(self):
        """if item does not exist in any of the lists should return false"""
        self.assertEqual(is_in_one('Tasabeeh',['Lina', 'Falaq', 'Rwan'],['x', 'y']), False)
#edge cases:
    def test_item_is_duplicated(self):
        """should work with duplicated items"""
        self.assertEqual(is_in_one('cat',['iron', 'dog', 'rat'],['cat','cat','banana']), True)
    def test_empty_lists(self):
        """test for empty list should return False"""
        self.assertEqual(is_in_one('cat',[],[]), False)
    def test_case_sensitivity(self):
        """test sensitivity for letter case """
        self.assertEqual(is_in_one('A',['a','b','c'],['b','d','f']), False)
#defensive tests:
    def test_item_is_not_string(self):
        """ should raise an error if item is not a string"""
        with self.assertRaises(AssertionError):
            is_in_one(123, ['t'], ['s'])
    def test_list1_is_not_list(self):
        """ should raise an error if list1 is not list"""
        with self.assertRaises(AssertionError):
            is_in_one('a', 'cat', ['d'])
    def test_list2_is_not_list(self):
        """ should raise an error if list2 is not list"""
        with self.assertRaises(AssertionError):
            is_in_one('a', ['d'], 'dog')
    
