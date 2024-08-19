#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize the maximum value with the first element
    max_val = my_list[0]

    # Iterate through the list to find the maximum value
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
