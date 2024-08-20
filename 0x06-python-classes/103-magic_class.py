#!/usr/bin/python3
import math


class MagicClass:
    """A class that represents a circle with methods to calculate its area
    and circumference."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius.

        Args:
            radius (float or int): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (float or int).
        """
        self.__radius = 0  # Initialize the radius attribute

        # Check if the radius is either an integer or a float
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        
        self.__radius = radius  # Set the radius if the type is valid

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return {self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
