#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle implementation
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x position
            y: y position
            id: object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        overriden __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def check(self, key, value, less_eq=True):
        """
        checks for value and type error
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(key))
        if less_eq:
            if value <= 0:
                raise ValueError("{} must be > 0".format(key))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(key))

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.check('width', width)
        self.__width = width

    @property
    def height(self):

