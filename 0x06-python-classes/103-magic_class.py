#!/usr/bin/python3
"""Module documentation for MagicClass class"""

import math


class MagicClass:
    """Class that mimics the provided Python bytecode"""

    def __init__(self, radius=0):
        """Initialization method"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Method to calculate the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Method to calculate the circumference"""
        return 2 * math.pi * self.__radius

