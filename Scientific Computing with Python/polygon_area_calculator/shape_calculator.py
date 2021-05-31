'''
This is my original code which completes the challenge project found at:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

The test modules and REPL can be found at:
https://replit.com/@samuelshoun/boilerplate-polygon-area-calculator-FCCfork
'''



import numpy as np

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50:
            return 'Too big for picture.'
        elif self.height > 50:
            return 'Too big for picture.'
        else:
            pic = []
            w_str = '*' * self.width
            for i in range(self.height):
                pic.append(w_str)
                pic.append('\n')
            return ''.join(pic)

    def get_amount_inside(self, shape):
        w_ct = np.floor(self.width / shape.width)
        h_ct = np.floor(self.height / shape.height)
        ct = int(h_ct * w_ct)
        return ct

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)



class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length
        self.side_length = side_length

    def set_width(self, w):
        self.width = w
        self.height = w
        self.side_length = w

    def set_height(self, h):
        self.width = h
        self.height = h
        self.side_length = h

    def __str__(self):
        return 'Square(side={})'.format(self.side_length)
