#!/usr/bin/python3

def no_c(my_string):
    new = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return(''.join(new))
