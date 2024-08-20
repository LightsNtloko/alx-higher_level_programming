#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []

    for k in range(list_length):
        try:
            # Attempt to get elements from both lists
            element_1 = my_list_1[k]
            element_2 = my_list_2[k]
            try:
                # Attempt division
                result.append(element_1 / element_2)
            except ZeroDivisionError:
                # Handle division by zero
                print("division by 0")
                result.append(0)
            except TypeError:
                # Handle wrong type in division
                print("wrong type")
                result.append(0)
        except IndexError:
            # Handle out of range for either list
            print("out of range")
            result.append(0)
        finally:
            # Optional cleanup or actions after the try block
            pass

    return result
