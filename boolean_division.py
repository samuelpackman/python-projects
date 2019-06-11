import numpy as np
import math as m
import random as r

"""n=10
m=5

a=np.random.randint(2, size=n)
b=np.concatenate((np.zeros((1,n-m)),np.random.randint(2, size=m)), axis=None)


def boolean_divide(a,b):
    b_1=b
    a_1=a
    while a_1[n-1] >=0:
        a_1 = a_1 - b_1
    return a_1

print(a)
print(b)
print(boolean_divide(a,b))"""

a = 32
b = 3
def binary_matrix(a,b):
    return np.vstack

def convert_binary(a):
    a_1=a
    list1 = []
    n = int(m.log(a,2)+1)
    for i in range(n):
        if 2 ** (n-i-1) <= a_1:
            a_1 -= 2 ** (n-i-1)
            list1 += [1]
        else:
            list1 += [0]
    return np.array(list1)

def convert_base10(a):
    sum1=0
    for i in range(len(a)):
        sum1 += 2 ** i * a[-1-i]
    return sum1

#def is_div_bin(M):
print(convert_base10(convert_binary(12)))
