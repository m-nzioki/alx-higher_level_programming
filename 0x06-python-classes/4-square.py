#!/usr/bin/python3

class Square:
    """ Defining a  class Square """
    def __init__(self, size=0):
        """ Initializing a square
        Args:
            size(int): Size of square
        """
        self.size = size

    @property
    def size(self):
        """ get/set size of current square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of a square """
        return (self.__size * self.__size)
