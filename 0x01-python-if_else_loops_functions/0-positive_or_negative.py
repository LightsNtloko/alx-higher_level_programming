#!/usr/bin/python3
import random
digit = random.randint(-10, 10)

if digit > 0:
    print(f"{digit} is positive")
elif digit == 0:
    print(f"{digit} is zero")
else:
    print(f"{digit} is negative")
