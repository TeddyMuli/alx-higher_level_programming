#!/usr/bin/python3

"""This is a class with a private attribute"""
class Square:
    """Constructor"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    """The area of the square"""
    def area(self):
        area = self.__size * self.__size
        return area