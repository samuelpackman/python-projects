import random
import numpy as np

class Board:
    def __init__(self):
        self.show = [[random.randint(1,100) for i in range(2)] for j in range(3)]
        self.lose = (self.show==3*[[1,1]])

    def __str__(self):
        return str(self.show)

    def move(self,place):
        if sum(place[1])!=self.show[place[0]][0] and sum(place[1])!=self.show[place[0]][1]:
            print("Invalid input: Not a partition, sums aren't correct")
            return False
        if False:#type(place[1][0]) != int or type(place[1][1]) != int or place[1][0] < 1 or place[1][1] < 1:
            print("Invalid input: Not a partition, aren't naturals")
            return False
        self.show[place[0]]=place[1]
        return not self.lose

    def game(self,func0,func1):
        bool1=True
        bool2=True
        while bool1:
            if bool2:
                bool1 = self.move(func1(self.show))
            else:
                bool1 = self.move(func0(self.show))
            bool2 = not bool2
        print("Player ",int(bool2)," has won!")
        return int(bool2)

def playgames(func0,func1,numgames):
    wins0=0
    wins1=0
    bool1=True
    for i in range(numgames):
        B = Board()
        if bool1:
            I = B.game(func0,func1)
            if I:
                wins1+=1
            else:
                wins0+=1
        else:
            I = B.game(func1,func0)
            if I:
                wins0+=1
            else:
                wins1+=1
    print("Out of ",numgames," games, Player0 won ",wins0," and Player1 won ",wins1,"!")
    return[wins0,wins1,numgames]

def MiloFunc(B):
    return 0

def SamFunc(B):
    print(B)
    print(np.array(B))
    A = np.array(B)
    A2 = np.zeros((3,2))
    for i in range(3):
        for j in range(2):
            A2[i:j] = A[i:j]%2

    if sum(sum(A2)) == 5:
        for j,i in enumerate(A2):
            if sum(i) == 1:
                print(i)
                return [j,[A[j:i[0]]-1,1]]

    return [0,[1, A[0:0]-1]]

print(playgames(SamFunc,SamFunc,30))
