#!/usr/bin/python3

""" Creating an empty class Rectangle """


class Rectangle:
    """ Defining Rectangle """
    def __init__(self, width=0, height=0):
        """ Initializing Rectangle
        Args:
            width(int): one side of rectangle
            height(int): other side of rectangle
        """
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """ Get/set width of current rectangle """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Get/set height of current rectangle """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """ Returns the area of a rectangle """
            return (self.__width * self.__height)

        def perimeter(self):
            return 0 if (self.__width == 0 or self.__height == 0) else \
                    2 * (self.__width + self.__height)

        def __str__(self):
            if self.__width == 0 or self.__height == 0:
                return ""
            return "\n".join(["#" * self.__width] * self.__height)

        def __repr__(self):
            return "Rectangle({}, {})".format(self.__width, self.__height)
