#!/usr/bin/python3
"""
Module to print the name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): First name.
        last_name (str): Last name (default is an empty string).

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith

    >>> say_my_name("Walter", "White")
    My name is Walter White

    >>> say_my_name("Bob")
    My name is Bob
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name).strip())

