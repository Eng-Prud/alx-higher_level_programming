#!/usr/bin/python3
"""
Define a rectangle class
"""


class Rectangle:
    """
    Represents a rectangle
    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        initializes a new Rectangle instance
        Args:
            width
            height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute
        Returns:
            int: width of rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute
        Args:
            Value(int): Value to set as width
        Raises:
             TypeError: if value is not int
             ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
