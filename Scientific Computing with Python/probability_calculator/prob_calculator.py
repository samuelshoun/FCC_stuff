'''
This is original code to complete the "Probability Calculator" challenge project at:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

The full solution with unit tests are found at:
https://replit.com/@samuelshoun/boilerplate-probability-calculator-FCCfork
'''




import numpy as np
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents_i = []
        for i,j in kwargs.items():
            for iter in range(j):
                self.contents_i.append(str(i))
        self.contents = self.contents_i.copy()

    def draw(self, num):
        if num <= len(self.contents):
            pass
        else:
            self.contents = self.contents_i.copy()

        if num > len(self.contents_i):
            num = len(self.contents_i)
        x = random.sample(self.contents, num)

        for i in x:
            self.contents.remove(i)
        return x



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    m = 0

    for i in range(num_experiments):
        drawn = Counter(hat.draw(num_balls_drawn))
        bools = []

        for k in expected_balls.keys():
            bools.append(drawn[k] >= expected_balls[k])

        if not False in bools:
            m += 1

    return m / num_experiments
