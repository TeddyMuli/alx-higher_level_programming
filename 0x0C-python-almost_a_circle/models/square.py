#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class inherited from the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor
        
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    #add public getter and setter size assigning width and height with the same height
    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size
        
        Args:
            value (int): The value to set the size to.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size <= 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    def update(self, *args, **kwargs):
        """Updates the Square with new attributes
        
        Args:
            *args (ints): The new attributes.
            **kwargs (dict): The new attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
    