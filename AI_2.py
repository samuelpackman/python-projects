import math
import random
import matplotlib.pyplot as plt
import numpy as np
# Get inputs to make my code
num_var = int(input('How many variables?'))
num_points = int(input('How many points?'))
#Randomly chose coordinates of my points
Points_x = []
Points_y = []
for i in range(num_points):
    Points_x.append(100 * random.random())
    Points_y.append(100 * random.random())

#randomly chose initial sttings of my AI
AI_Nodes = []
for i in range(num_var):
    AI_Nodes.append(random.random())

# evaluate polynomial
def Value(X):
    Point_Value = 0
    for k in range(num_var):
        Point_Value = Point_Value + (AI_Nodes[k] * (X ** k))
    return Point_Value

# Setting up a Cost function
def Cost():
    cost = 0
    for i in range (num_points):
        X = Points_x[i]
        Y = Points_x[i]
        cost = cost + (Value(X) - Y) ** 2
    return cost

# Set up back-propagation
def Backprop():
    global gradient
    for i in range(num_points):
        X = Points_x[i]
        Y = Points_x[i]
        for j in range(num_var):
            Value_Prime = 0
            AI_Nodes[j] = AI_Nodes[j] - ( 2 * ( Value(X) - Y) * (X ** j)) / 1000000
#Loop to find minimum
cost = 100000
k = -1
i = -1
gradient = 10 ** (num_var ** 2)
print(Cost())
while k != 1:
    i = i + 1
    if i % 10000000 == 0:
        x = np.linspace(0, 2, 100)
        plt.plot(x, Value(x), label='itterations = ' + str(i))
        plt.show()
    if i % 10 == 0:
        cost_1 = cost
    Backprop()
    cost = Cost()
    if cost_1 == cost:
        print ('local minimum has been found')
        k = 1
    print(Cost())
