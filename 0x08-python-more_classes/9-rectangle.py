#!/usr/bin/python3

"""A class for a rectangle"""
class Rectangle:
    """The public attributes"""
    number_of_instances = 0
    print_symbol = '#'

    """The constructor"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
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
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))       
    """Print Something"""
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    """The deconstructor"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    @classmethod
    def square(cls, size=0):
        return cls(size, size)