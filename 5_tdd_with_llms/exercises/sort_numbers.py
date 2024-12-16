def sort_numbers(nums: list) -> list:
    """This function takes a list of numbers and sorts them in ascending order.

    Args:
        nums (list): List of numbers (int, float)
    
    Raises:
        AssertionError: If `nums` is not a list
        AssertionError: If elements of `nums` are not numerical values

    Returns:
        list: Sorted list of numbers
    
    
        >>> sort_numbers([5, 3, 1, 2])
        [1, 2, 3, 5]
        >>> sort_numbers([-1, 9, 0])
        [-1, 0, 9]
        >>> sort_numbers([1.0, 3.0, 2.0])
        [1.0, 2.0, 3.0]
    """
    assert isinstance(nums, list), "Input must be a list"
    for item in nums:
        assert isinstance(item, (int, float)), "All elements in the list must be numerical values"
    return sorted(nums)
