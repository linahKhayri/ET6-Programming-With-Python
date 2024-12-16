""" Is in

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _at least one_ of the lists.

"""
def is_in(item:str,list1:list,list2:list) -> bool:
    """This function return a bool after checking if item is at least in one of the lists (return true) or not( return false)

Parameters:
item(str): we will look for the item in both lists and it has to be a string
list1(list): a list of string
list2(list): a list of string

return: returns a bool 

Raises:
AssertionError: if the fist parameter is not a string
AssertionError: if the second parameter is not a list
AssertionError: if the third parameter is not a list

>>> is_in('cat',['dog', 'cat', 'horse'],['rat', 'lion'])
True
>>> is_in('o', ['o', 'p'], ['s', 'o'])
True
>>> is_in('Lina',['lina','sara','falaq'],['i','o','t'])
False
"""
    assert isinstance(item, str)
    assert isinstance(list1,list)
    assert isinstance(list2,list)
    return item in list1 or item in list2
