#!/usr/bin/python3
<<<<<<< HEAD

def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit, end='')
=======
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end='')
>>>>>>> 0f49e8bc917e4349316aa4fea34bb5b34f068603
    return last_digit
