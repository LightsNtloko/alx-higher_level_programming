#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys and print each key-value pair
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
