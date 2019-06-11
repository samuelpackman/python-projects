def f(p,q):
    return p+q#random statement
def g(n):
    s = 0
    r=range(n)
    for i in r:
        for j in r:
            s += f(i,j)
    return s

#print(g(10))

import numpy

def h(n):
    return sum(f(index(i)) for i in j in numpy.random.rand((n,n)))

print(h(10))
