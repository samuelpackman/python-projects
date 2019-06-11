numbers = [1,6,7,8,3]
"""numbercombinations = 1
combinations = []
for i in inputlist:
    numbercombinations *= i
for i in range(numbercombinations):"""

def permutations(inputlist,firstelements = []):
    if not len(inputlist):
        return firstelements + inputlist
    else:
        return [permutations(inputlist[1:],firstelements + [i]) for i in range(inputlist[0])]

#print(permutations([2,2]))
def printvalues(output,temprange,linenum):
    print("output:" + str(output) + "temprange:" + str(temprange) + "linenum:" + str(linenum))

def p(l):
    o = []
    n = 1
    t = [0 for i in l]
    t[0] = -1
    for i in l:
        n *= i
    for i in range(n):
        t[0] += 1
        k = 0
        for j in t:
            if l[k] == j:
                t[k] = 0
                t[k+1] += 1
            k += 1
        o += [[i for i in t]]
    return o

print(p([2,2]))
 *
