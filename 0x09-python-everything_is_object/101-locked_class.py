#!/usr/bin/python3
"""Locked Class"""
class LockedClass:
    """THE OBJECTS"""
    __slots__ = ["first_name"]
    """The objects"""
    def __setattr__(self, name, value):
        """The object"""
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)