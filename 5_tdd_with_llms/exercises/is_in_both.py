""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.

"""
def is_in_both(item:str,list1:list,list2:list) -> bool:
    """This function return a bool after checking 
      weather item in both lists (return true) or not(return false)

Parameters:
item(str): we will look for the item in both lists
list1(list): a list of string
list2(list): a list of string

return: returns a bool value

Raises:
AssertionError: if the fist parameter is not a string
AssertionError: if the second parameter is not a list
AssertionError: if the third parameter is not a list

>>> is_in_both('cat',['dog', 'cat', 'horse'],['cat', 'lion'])
True
>>> is_in_both('o', ['o', 'p'], ['s', 'p'])
False
  """
    assert isinstance(item, str)
    assert isinstance(list1,list)
    assert isinstance(list2,list)
    return item in list1 and item in list2 
    
  