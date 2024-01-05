#!/usr/bin/python3


"""This is a class with a private attribute"""
class Square:
    """Constructor"""
    def __init__(self, size=0, position=(0 ,0)):
        self.size = size
        self.position = position
    """The getter"""
    @property
    def size(self):
        return self.__size
    """The setter"""
    @size.setter    
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """Getter"""
    @property
    def position(self):
        return self.__position
    """Setter"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """Area"""
    def area(self):
        return (self.size) ** 2
    """Print"""
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)