#!/usr/bin/python3
"""A class for a rectangle"""
class Rectangle:
    """The constructor"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """The getter"""
    @property
    def width(self):
        return self.__width
    """The setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    """The getter"""
    @property
    def height(self):
        return self.__height
    """The setter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value