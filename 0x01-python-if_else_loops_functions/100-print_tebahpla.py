#!/usr/bin/python3

print("".join(
    "{:c}".format(122 - i if i % 2 == 0 else 90 - i)
    for i in range(26)
), end='')
