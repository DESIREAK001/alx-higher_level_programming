#!/usr/bin/python3
def magic_string():
    return "BestSchool" * (magic_string.iteration or 1)
magic_string.iteration = 0
