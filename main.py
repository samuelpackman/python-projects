primes = [2]

Max = 100000

root_10 = 10 * .5

lines = [[(root_10 -1) / 9 , 1 , 1] , [(1 - 1 / root_10) / 9 , 100 , 10]]


'''def sqrt( x , m , x_0 , y_0):
    a = m * (x - x_0) + y_0
    for i in range(2):
        a = a / 2 - x / 2 * a
    return a'''

def magnitude(x):
    k = 0
    while x > 0:
        x = x // 10
        k = k + 1
    return k

def approxi_root(x , index):
    Line = lines[index]
    return Line[0] * ( x - Line[1]) + Line[2]

print(approxi_root(67 , 1))
print(67 ** .5)

'''for i in range(3,Max):
    R = 1
    k = 0
    while primes[k] <= int(sqrt(i)):
        if i % primes[k] == 0:
            R = 0
            pass
        k = k + 1
    if R == 1:
        primes.append(i)

print(primes)'''
