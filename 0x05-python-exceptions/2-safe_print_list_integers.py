#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while True:
        try:
            # Try to access the i-th element
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                count += 1
            i += 1
            if i >= x:
                break
        except IndexError:
            # Print traceback message on stderr
            import sys
            print("Traceback (most recent call last):", file=sys.stderr)
            sys.exit(1)  # Exit with an error code to indicate failure
    print()
    return count
