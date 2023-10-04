#!/usr/bin/python3
"""say_my_name module"""


def say_my_name(first_name, last_name=""):
    """Return the name of the person.
    Args:
        first_name (str): The first name.
        last_name (str): The last name
    Raises:
        TypeError: If first_name or last_name is not a string
    Return:
        The name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
