#!/usr/bin/python3

def pow(a, b):
    """Computes a to the power of b and returns the result."""
    if b == 0:
        return 1
    elif b > 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    else:
        result = 1
        for _ in range(-b):
            result *= a
        return 1 / result
