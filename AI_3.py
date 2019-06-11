import random
import math

Data = [[[ (x == y and 1 or 0) for x in range(4)] for i in range(4)] for y in range(4) ] + [[[ (i == y and 1 or 0) for x in range(4)] for i in range(4)] for y in range(4) ] + [[[ ( ( abs(x - 1) <= 1 and abs(y - y2) <= 1 and not (abs(x - 1) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4) ] for y in range(4)] for y2 in range(1, 3) ] + [[[ ( ( abs(x - 2) <= 1 and abs(y - y2) <= 1 and not (abs(x - 2) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4) ] for y in range(4)] for y2 in range(1, 3) ] + [[[ ( ( abs(x - x2) == 1 or abs(x - x2) == 0 and (y == 0 or y == 3)) and 1 or 0) for x in range(4) ] for y in range(4)] for x2 in range(1, 3) ] + [[[ ( ( abs(y - y2) == 1 or abs(y - y2) == 0 and (x == 0 or x == 3)) and 1 or 0) for x in range(4) ] for y in range(4)] for y2 in range(1, 3) ]
Key = [[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]

L_1_weights = []

for i in range(16):
    I = []
    for j in range(8):
        I.append(random.random())
    L_1_weights.append(I)

L_2_weights = []

for i in range(8):
    I = []
    for j in range(2):
        I.append(random.random())
    L_2_weights.append(I)

def sigmoid(x):
    return 1 / ( 1 + math.exp( 0 - x))

def sigmoid_prime(x):
    return (sigmoid(x) ** 2) * math.exp(0 - x)

def Propagate(k,b):
    L_2_activations = []
    for n in range(8):
        K = 0
        for i in range(16):
            K = K + L_1_weights[i][n] * Data[k][i // 4][i % 4]
        L_2_activations.append(sigmoid(K))
    if b == 1:
        return L_2_activations
    L_1_activations = []
    for n in range(2):
        K = 0
        for i in range(8):
            K = K + L_2_weights[i][n] * L_2_activations[i]
        L_1_activations.append(sigmoid(K))
    return L_1_activations

def Partial_Cost(k):
    N = Propagate(k,0)
    return (N[0] - Key[k][0]) ** 2 + (N[1] - Key[k][1]) ** 2

def Cost():
    cost = 0
    for i in range(len(Data)):
        cost = cost + Partial_Cost(i)
    return cost

def derivative_L_2(num_data,i,k):
    W = 0
    N = Propagate(num_data,0)
    L_2 = Propagate(num_data,1)
    for j in range(8):
        W = W + L_2[j] * L_2_weights[j][k]
    return (N[k] - Key[num_data][k]) * sigmoid_prime(W) * L_2[i]

def derivative_L_1(num_data,i,k):
    W = 0
    L_1 = Data[num_data]
    L_2 = Propagate(num_data,1)
    for j in range(16):
        W = W + L_1[j // 4][j % 4] * L_1_weights[j][k]
    return (
    derivative_L_2(num_data,k,0) / L_2[0] * L_2_weights[i][0] * sigmoid_prime(W) * L_1[i // 4][i % 4] +
    derivative_L_2(num_data,k,1) / L_2[1] * L_2_weights[i][1] * sigmoid_prime(W) * L_1[i // 4][i % 4]
    )



def Backprop():
    for data in range(16):
        for i in range(16):
            for k in range(8):
                L_1_weights[i][k] = L_1_weights[i][k] - derivative_L_1(data,i,k)/10 ** 5
        for i in range(8):
            for k in range(2):
                L_2_weights[i][k] = L_2_weights[i][k] - derivative_L_2(data,i,k) /10 ** 5

cost = 100000
o = -1
p = -1
Backprop()
print(Cost())
while o != 1:
    p = p + 1
    if p % 10 == 0:
        cost_1 = cost
    cost = Cost()
    if cost_1 == cost:
        print ('local minimum has been found')
        o = 1
    print(Cost())
