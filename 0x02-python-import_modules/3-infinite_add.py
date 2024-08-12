#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Initialize the sum to 0
    total = 0
    
    # Iterate over all arguments (excluding the script name itself)
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert argument to integer and add to total
    
    # Print the result
    print(total)
