def lint(list1):
    while type(list1) == list:
        list1 = list1[0]
    return list1

class circuit:
    def __init__(self,array):
        self.board = array

    def __str__(self):
        return str(self.board)

    def run(self,A):
        temparray = A
        if self.board == "not":
            return (1 + lint(A[0]))%2
        if self.board == "or":
            return (lint(A[0]) + lint(A[1]) + lint(A[0]) * lint(A[1]))%2
        if self.board == "value":
            return lint(A[0])
        else:
            for row in self.board:
                temparray = [comp[0].run([temparray[i] for i in comp[1:]]) for comp in row]
            return [lint(i) for i in temparray]

not_ = circuit("not")
or_ = circuit("or")
value_ = circuit("value")

and_ = circuit([
[[not_,0],[not_,1]],
[[or_,0,1]],
[[not_,0]]
])

xor_ = circuit([
  [[and_,0,1],[or_,0,1]],
  [[not_,0],[value_,1]],
  [[and_,0,1]]
  ])

bit1add_ = circuit([
[[and_,0,1],[xor_,0,1]]
])

class recircuit:
    def __init__(self,base_,n):
        self.reclevel = n
        self.base = base

    def rerun(self,A):
        temparray = A
        returnarray = []
        for i in range(self.reclevel)
            if i == 1:
                returnarray = self.base.run(temparray) + returnarray
