#!/usr/bin/python3
import importlib


def magic_calculation(a, b):
    # Dynamically import the module and functions
    calc_module = importlib.import_module('magic_calculation_102')
    add = getattr(calc_module, 'add')
    sub = getattr(calc_module, 'sub')

    if a < b:
        # Perform the addition operation
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
