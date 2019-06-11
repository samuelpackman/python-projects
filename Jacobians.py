import math as m
import numpy as np
import random as r

Data = np.array([[ (x == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ (i == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ ( ( abs(x - 1) <= 1 and abs(y - y2) <= 1 and not (abs(x - 1) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - 2) <= 1 and abs(y - y2) <= 1 and not (abs(x - 2) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - x2) == 1 or abs(x - x2) == 0 and (y == 0 or y == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for x2 in range(1, 3) ] + [[ ( ( abs(y - y2) == 1 or abs(y - y2) == 0 and (x == 0 or x == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ])
Key = np.array([[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]])

W=np.random.rand(8,16)    #weights for layer one
X=np.random.rand(2,8)     #weights  for layer two
#print(W)
num_data=0

def esigmoid(A):
    return A/(A+ A*np.exp(-1*A))

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

def Jh(num_data,W):
    return np.tile(Data[num_data,:],(8,1))*np.rot90(np.tile(esigmoidprime(np.dot(W,Data[num_data,:])),(16,1)),3)

def Jo(h,X):
    return np.tile(h,(2,1))*np.rot90(np.tile(esigmoidprime(np.dot(X,h)),(8,1)),3)

def Jc(num_data,o):
    return 2*(o-Key[num_data,:])

def PropogateW():
    return  W + 1/100 * np.tile(Jc(num_data,o(h(num_data,W),X))@Jo(h(num_data,W),X)@Jh(num_data,W),(8,1) )

def PropogateX():
    return X + 1/100 * np.tile(Jc(num_data,o(h(num_data,W),X))    @ Jo(h(num_data,W),X),(2,1))


#print(      Jc(2,o(h(2,W),X))    @ Jo(h(2,W),X)         @ Jh(2,W)         )
#print(Jh(num_data,W))
#print(X@W)
#print(Jc(num_data,o(h(num_data,W),X))    @ Jo(h(num_data,W),X))
#print(Jh(2,W))
#print(      Jc(num_data,o(h(num_data,W),X))    @ Jo(h(num_data,W),X)         @ Jh(num_data,W)         )
