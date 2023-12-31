#!/usr/bin/python3

"""Defining an empty class Square."""


class Square:
    """ Defining a  class Square """
    def __init__(self, size=0):
        """ Initializing square
        Args:
            size(int): Size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
