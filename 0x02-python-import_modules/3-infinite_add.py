#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Initialize the sum to 0
    total = 0

    for arg in sys.argv[1:]:
        total += int(arg)

    print(total)
