"""A module for numbers manipulation focusing on giving the sum of two numbers
Module contents:
    - sum_value: give the sum of two numerical values (int or float)
created on 2024-12-12
Author: Linah Khayri
"""
def sum_numbers(num1,num2) -> (int,float):
    """This function takes two numbers and return the sum of the numbers given


    Args:
        num1 (int,float): first number must be an int or float
        num2 (int,float): second number must be an int or float

    Returns:
        sum: (int,float): the sum of the two numbers
        
    Raises:
        AsserionError: if input is not a number int or float
        >>> sum_numbers(3,5)
        8
        >>> sum_numbers(2.0,1)
        3.0
        >>> sum_numbers(1.0,4.0)
        5.0
    """
    assert isinstance(num1,(int,float))
    assert isinstance(num2,(int,float))
    return num1+num2
