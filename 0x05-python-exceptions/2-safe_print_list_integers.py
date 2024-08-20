#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Check if the index is within the bounds of the list
            if i >= len(my_list):
                raise IndexError
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError:
        # Print traceback message on stderr
        import sys
        print("Traceback (most recent call last):", file=sys.stderr)
        sys.exit(1)  # Exit with an error code to indicate failure
    print()
    return count
