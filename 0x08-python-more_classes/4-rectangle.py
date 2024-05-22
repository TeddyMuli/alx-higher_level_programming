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
    """Area"""
    def area(self):
        return self.__height * self.__width
    """Perimeter"""
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            per = 0
        else:
            per = (self.__height + self.__width) * 2

        return per
    """Print Rectangle"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    """"""
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
