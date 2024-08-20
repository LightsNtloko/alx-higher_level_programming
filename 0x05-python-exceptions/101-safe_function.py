#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # Execute the function with the given arguments
        return fct(*args)
    except Exception as e:
        # Print the exception message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return None
