#!/usr/bin/python3
def add_integer(a, b=98):
    if not (isinstance(a, (int, float))) and (isinstance (b, (int, float))): 
        raise TypeError("a must be integers" or "b must be an integer")
    if (isinstance (a, (int, float))) and (instance(b,(int, float)))):
    a = int(a)
    b = int(b)
    return a+b
