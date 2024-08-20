#!/usr/bin/python3
"""Define a class Square with a private attribute."""

class Square:
    """A class that defines a square with a private attribute for size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
