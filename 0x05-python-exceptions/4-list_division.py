#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Check if both indices are within the range of the lists
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            # Check if elements are numbers (int or float)
            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                try:
                    # Perform the division
                    result.append(element_1 / element_2)
                except ZeroDivisionError:
                    # Handle division by zero
                    print("division by 0")
                    result.append(0)
            else:
                # Handle wrong type
                print("wrong type")
                result.append(0)
        except IndexError:
            # Handle case where index is out of range for either list
            print("out of range")
            result.append(0)

    return result
