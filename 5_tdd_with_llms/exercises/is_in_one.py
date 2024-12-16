""" Is in one

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _only one_ of the lists.

"""

def is_in_one(item:str,list1:list,list2:list) -> bool:
    """This function return a bool after checking 
    weather item in both lists (return true) or not( return false)

Parameters:
item(str): we will look for the item in both lists and it has to be a string
list1(list): a list of string
list2(list): a list of string

return: returns a bool 

Raises:
AssertionError: if the fist parameter is not a string
AssertionError: if the second parameter is not a list
AssertionError: if the third parameter is not a list

>>> is_in_one('cat',['dog', 'cat', 'horse'],['rat', 'lion'])
True
>>> is_in_one('o', ['o', 'p'], ['s', 'o'])
False
>>> is_in_one('Lina',['lina','sara','falaq'],['i','o','t'])
False
"""
    assert isinstance(item, str)
    assert isinstance(list1,list)
    assert isinstance(list2,list)
    
    if item in list1 and item in list2:
        return False
    elif item in list1:
        return True
    elif item in list2:
        return True
    else:
        return False
