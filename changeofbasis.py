import numpy as np
import cmath as m
import random as r
import sympy as sp
from sympy import symbols

dim=2
x=symbols('x')
A=sp.Matrix(np.random.rand(dim,dim))

def eigenvalues(A):
    A-= sp.Matrix(x*np.identity(int(np.size(A)**0.5)))
    A=A.det()

#print((A- sp.Matrix(x*np.identity(int(np.size(A)**0.5))).det()))
A-= sp.Matrix(x*np.identity(int(np.size(A)**0.5)))
a=A.det()
y=sp.solve(a,x)
print(y)
#for i in y:
