#!/usr/bin/python3

"""This is a class with a private attribute"""
class Square:
    """Constructor"""
    def __init__(self, size=0):
        self.size = size
    """Getter"""
    @property
    def size(self):
        return self.__size
    """Setter"""
    @size.setter    
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """The area"""
    def area(self):
        return (self.__size) ** 2