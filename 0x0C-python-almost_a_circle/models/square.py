#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """ str """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """ update """
        if args and len(args) == 0:
            return
        elif len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value

    def to_dictionary(self):
        """ to_dictionary """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
