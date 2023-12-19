#!/usr/bin/python3
"""Module documentation for Square class"""


class Square:
    """Class to define a square"""

    def __init__(self, size=0):
        """Instantiation with size"""
        self.size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator"""
        return self.area() >= other.area()
