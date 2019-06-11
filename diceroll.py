import random
def diceroll(n):
    r = random.randint(1,n)
    if r > 1:
        return r
    return diceroll(n) + diceroll(n)
k,n = 10**5,6

def evendiceroll(n):
    sum1 = 0
    i = 0
    while sum1%2 == 0:
        i += 1
        sum1 = sum([random.randint(1,n) for j in range(i)])
    return sum1

print(sum([evendiceroll(n)/k for i in range(k)]))
