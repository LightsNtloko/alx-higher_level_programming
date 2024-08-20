#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Remove the key from the dictionary if it exists
    if key in a_dictionary:
        del a_dictionary[key]
    # Return the modified dictionary
    return a_dictionary
