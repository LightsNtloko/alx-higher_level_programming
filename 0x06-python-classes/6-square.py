#!/usr/bin/python3
"""Define a class Square with size and position attributes and methods to
calculate area and print the square."""


class Square:
    """A class that defines a square with private size and position
    attributes and methods for area and printing."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance with optional size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square (x, y). Defaults to
            (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
            of 2 positive integers.
            ValueError: If size is less than 0 or position values are
            negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): The new position of the square (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(k, int) for k in value) or
            not all(k >= 0 for k in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #, respecting the position.

        Prints:
            A square of size self.__size by self.__size using #.
            If size is 0, prints an empty line.
            Position is used to add spaces before the square.
        """
        if self.__size == 0:
            print()
            return

        # Print leading newlines based on position[1]
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            # Print leading spaces based on position[0]
            print(' ' * self.__position[0] + '#' * self.__size)
