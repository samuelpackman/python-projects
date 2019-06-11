import random
import math
import numpy as np

Data = np.array([[ (x == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ (i == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ ( ( abs(x - 1) <= 1 and abs(y - y2) <= 1 and not (abs(x - 1) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - 2) <= 1 and abs(y - y2) <= 1 and not (abs(x - 2) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - x2) == 1 or abs(x - x2) == 0 and (y == 0 or y == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for x2 in range(1, 3) ] + [[ ( ( abs(y - y2) == 1 or abs(y - y2) == 0 and (x == 0 or x == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ])
Key = [[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]

print(Data)

L_1_weights = np.random.rand(8,16)
L_2_weights = np.random.rand(2,8)

def sigmoid(x):
    return 1 / ( 1 + math.exp( 0 - x))

def sigmoid_prime(x):
    return (sigmoid(x) ** 2) * math.exp(0 - x)


def Propagate(num_data,b):

    Hidden_layer = []
    for i in range(8):
        Hidden_layer.append(sigmoid(np.dot(Data[num_data],L_1_weights[i])))

    Outputs = []
    for i in range(2):
        Outputs.append(sigmoid(np.dot(Hidden_layer,L_2_weights[i])))

    if b == 0:
        return Hidden_layer
    if b == 1:
        return Outputs

def Data_Cost(num_data):
    Outputs = Propagate(num_data,1)
    return (Outputs[0] - Key[num_data][0]) ** 2 + (Outputs[1] - Key[num_data][1]) ** 2

def Cost():
    cost = 0
    for i in range(len(Data)):
        cost = cost + Data_Cost(i)
    return cost

def derivative_hidden_out(num_data,hidden,output):

    Hidden_layer = Propagate(num_data,0)
    Outputs = Propagate(num_data,1)

    Sum = 0
    for i in range(8):
        Sum = Sum + Hidden_layer[i] * L_2_weights[i][output]
    return 2 * (Outputs[output] - Key[num_data][output]) * sigmoid_prime(Sum) * Hidden_layer[hidden]
