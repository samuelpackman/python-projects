import random
import time

class point:

    def __init__(self, X , Y):
        self.zero = (X ** 2 + Y ** 2) ** .5
        self.x = X
        self.y = Y
    def __str__ (self):
        return 'x = ' + str(self.X) + 'y = ' + str(self.Y)

point_number = int(input('How many points? '))
Points = []
for i in range(point_number):
    a = point(10 * random.random() , 10  * random.random())
    Points.append(a)
m = 1
b = 1
def Cost():
    global m
    global b
    cost = 0
    for i in range(point_number):
        current = Points[i]
        X = current.x
        Y = current.y
        cost = cost + ( m * X + b - Y) ** 2
    return cost

def Backprop():
    global m
    global b
    m_change = 0
    b_change = 0
    for i in range(point_number):
        current = Points[i]
        X = current.x
        Y = current.y
        m_change = m_change + 2 * ( m * X + b - Y) * X
        b_change = b_change + 2 * ( m * X + b - Y)
    m = m - m_change / 1000
    b = b - b_change / 1000

cost = 200
k = 0

while k != 1:
    cost_1 = cost
    Backprop()
    cost = Cost()
    if cost_1 == cost:
        print ('local minimum has been found')
        k = 1
        print(Cost())
