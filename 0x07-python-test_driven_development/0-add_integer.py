#!/usr/bin/python3

"""An integer addition function"""


def add_integer(a, b=98):
    """Returns sum of a and b
    floats are type-casted to ints before addition

    Raises:
        TypeError if a or b is a non int or non float
    """

    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    if ((not isinstance(a, float) and not isinstance(a, int))):
        raise TypeError("a must be an integer")

    return (int(a) + int(b))
