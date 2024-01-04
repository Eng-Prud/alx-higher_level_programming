#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Defines class Rectangle with private attributes: width aand height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of an instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """ Returns height of a Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height of a Rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Return distance round the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
