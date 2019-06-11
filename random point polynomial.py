

import random as r
import numpy as np
num_points=int(input("How many points"))
y=np.zeros(1,num_points)
a=np.zeros(num_points,num_points)
for i in range(num_points):
    y[i]=(0.5-r.random())/(r.random()-0.5)
    for j in range(num_points):
        a[i,j]=(0.5-r.random())/(r.random()-0.5)
