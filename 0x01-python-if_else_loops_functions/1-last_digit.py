#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
the_string = "Last digit of {} is {}".format(number, lastdigit)
if lastdigit > 5:
    print("{the_string} and is greater than 5")
elif lastdigit == 0:
    print("{the_string} and is 0")
else:
    print("{the_string} and is less than 6 and not 0")
