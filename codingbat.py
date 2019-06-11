"""We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done"""
import time
import random

def make_chocolate(s, b, g):
  if 5*b>=g:
    if s>=g%5:
      return g%5
    else:
      return -1
  elif s>=g-5*b:
    return g-5*b
  else:
    return -1

def make(small,big, goal):
    """    if 5*big+small<goal:
        return -1
    g = goal//5
    if big<g:
        goal -= 5*big
    else:
        goal -= 5*g

    if small < goal:
        return -1
    return goal
    print([random.random() for i in range(1000000)])"""
    return 1
n=10**5
time_0 = time.time()

for i in range(n):
    a = make_chocolate(random.randint(0,n),random.randint(0,n),random.randint(0,n))

time_1 = time.time()

print(time_1-time_0)

time_2 = time.time()

for i in range(n):
    a = make(random.randint(0,n),random.randint(0,n),random.randint(0,n))

time_3 = time.time()

print(time_3 - time_2)
