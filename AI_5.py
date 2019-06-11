import math as m
import numpy as np
import random as r

Data = np.array([[ (x == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ (i == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ ( ( abs(x - 1) <= 1 and abs(y - y2) <= 1 and not (abs(x - 1) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - 2) <= 1 and abs(y - y2) <= 1 and not (abs(x - 2) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - x2) == 1 or abs(x - x2) == 0 and (y == 0 or y == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for x2 in range(1, 3) ] + [[ ( ( abs(y - y2) == 1 or abs(y - y2) == 0 and (x == 0 or x == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ])
Key = np.array([[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]])

W=np.random.rand(8,16)    #weights for layer one
X=np.random.rand(2,8)     #weights  for layer two
gradient_weight = 10**5

def iteration_order(i):
    index = [0,15,2,14,2,13,3,12,4,11,5,10,6,9,7,8]
    return index[i]

def div0( a, b ):
    """ ignore / 0, div0( [-1, 0, 1], 0 ) -> [0, 0, 0] """
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide( a, b )
        c[ ~ np.isfinite( c )] = 0  # -inf inf NaN
    return c

def esigmoid(A):
    B=np.ones(np.size(A))
    return np.divide(B,(B + np.exp(-1*A)))  # 1/(1 + np.exp(-1*A))

def esigmoidprime(A):
    return esigmoid(A) * esigmoid(A) * np.exp (-1*A)

def h(num_data,W):
    return esigmoid(np.dot(W,Data[num_data,:]))

def o(h,X):
    return esigmoid(np.dot(X,h))

def c(num_data,o):
    return np.dot(o - Key[num_data,:],o - Key[num_data,:])

def cost(num_data,W,X):
    return c(num_data,o(h(num_data,W),X))

def total_cost(W,X):
    sum1=0
    for i in range(len(Data)):
        sum1+=cost(i,W,X)
    return sum1
#print(h(15,W))

def Jh(num_data,W):
    return np.tile(Data[num_data,:],(8,1))*np.rot90(np.tile(esigmoidprime(np.dot(W,Data[num_data,:])),(16,1)),3)

def Jo(h,X):
    return np.tile(h,(2,1))*np.rot90(np.tile(esigmoidprime(np.dot(X,h)),(8,1)),3)

def Jc(num_data,o):
    return 2*(o-Key[num_data,:])

#print((Jc(1,o(h(1,W),X)) @ Jo(h(1,W),X)@Jh(1,W))[0])

'''def dW(num_data,W,X):
    gradient = Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X)@Jh(num_data,W)
    for i in range(len(gradient)):
        if gradient[i] == 0:
            gradient[i]=10000
    return np.array(gradient)

def dX(num_data,W,X):
    gradient = Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X)
    for i in range(len(gradient)):
        if gradient[i] == 0:
            gradient[i]=10000
    return np.array(gradient)'''



#num_data=2

#print(np.tile(Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X)@Jh(num_data,W),(8,1) ))
#print(div0(np.ones((8,16)),np.tile(Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X)@Jh(num_data,W),(8,1) )))

"""def PropogateW(num_datsa):
    return  np.array((99/100 * W) + (1/100 * (W - cost(num_data,W,X) * np.divide(np.ones((8,16)),np.tile(np.ones((1,16))+Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X)@Jh(num_data,W),(8,1) )))))

def PropogateX(num_data):
    return  np.array((99/100 * X) + (1/100 * (X - cost(num_data,W,X) * np.divide(np.ones((2,8)),np.tile(np.ones((1,8))+Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X),(2,1))))))"""

def PropogateW(num_data):
    return  W - 1/gradient_weight * cost(num_data,W,X) * div0(np.ones((8,16)),np.tile(Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X)@Jh(num_data,W),(8,1) ))

def PropogateX(num_data):
    return  X - 1/gradient_weight * cost(num_data,W,X) * div0(np.ones((2,8)),np.tile(Jc(num_data,o(h(num_data,W),X)) @ Jo(h(num_data,W),X),(2,1)))

cost_1=-1
cost_2=-1
l = -1
p = -1
print(total_cost(W,X))

while l != 1:
    p = p + 1
    for i in range(16):
        W = PropogateW(iteration_order(i))
        X = PropogateX(iteration_order(i))
    if p%10==0:
        gradient_weight =  10**(min(5,15-total_cost(W,X)))
        if abs(cost_1 - total_cost(W,X)) < 10**-6:
            if cost_1>=9:
                W=100 * (np.random.rand(8,16) - 1/2 * np.ones((8,16)))
                X=100 * (np.random.rand(2,8) - 1/2 * np.ones((2,8)))
            else:
                print ('local minimum has been found')
                l = 1
                print(total_cost(W,X))
        else:
            cost_1=total_cost(W,X)

        print(total_cost(W,X))
    if p%50==0:
        if True:#abs(cost_2-total_cost(W,X))<10**-3:
            W=100 * (np.random.rand(8,16) - 1/2 * np.ones((8,16)))
            X=100 * (np.random.rand(2,8) - 1/2 * np.ones((2,8)))
        cost_2=total_cost(W,X)
        #print(total_cost(W,X))

print(W)
print(X)
