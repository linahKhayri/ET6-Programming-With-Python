""" Sum Evens and Odds

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""
def sum_evens_and_odds(numbers: list) -> dict:
    """This function takes any list of numbers and returns a dictionary with the sum of the even and odd numbers.

    Args:
        numbers (list): A list of numbers (int or float).

    Returns:
        dict: A dictionary containing the sum of even and odd numbers.
    
    Raises:
        AssertionError: If the input is not a list.
        AssertionError: If the items in the list are not numbers.

    >>> sum_evens_and_odds([1, 2, 3, 4, 5])
    {'sum_even': 6, 'sum_odd': 9}
    >>> sum_evens_and_odds([0, 2, 4, 5])
    {'sum_even': 6, 'sum_odd': 5}
    >>> sum_evens_and_odds([])
    {'sum_even': 0, 'sum_odd': 0}
    >>> sum_evens_and_odds([1.0, 2.0, 5.0])
    {'sum_even': 2.0, 'sum_odd': 6.0}
    """
    # the input must be a list
    assert isinstance(numbers, list)

    
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        # Check if each item in the list is a number (int or float)
        assert isinstance(number, (int, float))

        
        # Check if the number is even or odd and sum accordingly
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return {'sum_even': even_sum, 'sum_odd': odd_sum}
