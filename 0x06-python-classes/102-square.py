#!/usr/bin/python3
"""Define a class Square based on 4-square.py with additional comparator
methods."""


class Square:
    """A class that defines a square with private size attribute, methods for
    area calculation, and comparator methods based on square area."""

    def __init__(self, size=0):
        """Initialize a new Square instance with optional size.

        Args:
            size (float or int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality between two squares based on their area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare inequality between two squares based on their area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if this square is less than another square based
        on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if this square is less than or equal to another square based
        on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if this square is greater than another square based
        on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if this square is greater than or equal to another square
        based on area."""
        return self.area() >= other.area()
