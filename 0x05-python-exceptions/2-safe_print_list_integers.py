#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        while i < x:
            # Attempt to access the i-th element
            element = my_list[i]
            # Check if the element is an integer
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                count += 1
            i += 1
    except IndexError:
        import traceback
        traceback.print_exc()
    print()  # Print newline after the output
    return count
