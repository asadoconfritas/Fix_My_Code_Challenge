#!/usr/bin/python3
"""
comment
"""

class square():
    """comment square"""
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """init method"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """perimeter of sq"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """str format"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """comment"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
