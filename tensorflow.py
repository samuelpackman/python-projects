import numpy as np
import random
#Sigmoid function
def sig(x,booly):
    a=1/5
    if not booly:
        return 1/(1+np.exp(a*x))
    return a*np.exp(-a*x)*sig(x,False)**2
#Nested loops
def RecLoop(I,O=[]):
    if I:
        if not O:
            O=[[i] for i in range(I[0])]
            I=I[1:]
            if not I:
                return O
        O=RecLoop(I[1:],[E+[i] for i in range(I[0]) for E in O])
    return O

def sigmoid_prime_of_sigmoid(sigmoid):
    return a * (sigmoid - sigmoid**2)
# An input layer
class Input:

    def __init__(self,size,name="Noone"):
        self.name=name
        self.size=size
        self.body= np.empty((size),dtype=int)

    #Plugs in input data
    def run(self,data):
        if len(data) != self.size:
            print("Error: Misized input in input layer " + self.name)
        self.body=[data[i] for i in range(self.size)]

    def __str__(self):
        return self.name+"| type=InputLayer | size= " +str(self.size)+"| "+ str(self.body)
# A hidden Layer
class Hidden:

    def __init__(self,size,InLayer,name="Noone"):
        self.name=name
        self.size=size
        self.In=InLayer
        self.weights=[[10*random.random()-5 for i in range(InLayer.size)] for i in range(size)]
        self.body=[None for i in range(size)]

    def wSum(self,i):
        sum1=0
        for j in range(self.In.size):
            sum1+=self.weights[i][j]*self.In.body[j]
        return sum1

    #Forward propagation
    def run(self):
        for i in range(self.size):
            self.body[i]=sig(self.wSum(i),False)

    def __str__(self):
        return self.name+"| type=HiddenLayer | size="+str(self.size)+"| " + str(self.body)
# A full network
class Network:

    def __init__(self,Arrays,name="Noone"):
        self.size=len(Arrays)
        self.name=name
        self.Layers=[Input(Arrays[0],name+"L0")]
        for i in range(1,len(Arrays)):
            temp=Hidden(Arrays[i],self.Layers[-1],name+"L"+str(i))
            self.Layers.append(temp)

    #Full forwards propagation
    def run(self,data):
        self.Layers[0].run(data)
        for i in range(1,self.size):
            self.Layers[i].run()
    #Backprop
    def cost(self,label):
        cote=0
        for i in range(len(label)):
            cote+=(label[i]-self.Layers[-1].body[i])**2
        return cote
    #Partial partial derivative
    def partial(self,n,data):
        pass
        
    def Jacobian(self,n): #collumns are df_i for every i, rows for dx_j for every j every f_i included in each collumn
        Weights = np.array(self.Layers[n+1].weights)
        output_nodes = self.Layers[n+1].body
        input_dim = len(self.Layers[n]) # i is index of input node, j is index of output node
        output_dim= len(self.Layers[n+1])    #outputmatrix = np.zeros((inputdim,output_dim))  #not actually used just notes
        Jacobian_sigmoids = np.array[[[sigmoid_prime_of_sigmoid(output_nodes[j])] for j in range(output_dim)] for i in range(inputdim)] #stacked matrix of all the sigmoid_primes in each collumn
        return Weights * Jacobian_sigmoids

    #Full partial derivative
    def train(self,InData,data,delta):
        pass
        """
        self.run(InData)
        for n in range(1,self.size-1):
            for i in range(self.Layers[n].size):
                for j in range(self.Layers[n+1].size):
                    self.Layers[n].weights[i][j]-=delta*self.partial(n,i,j,data)
        """

    def __str__(self):
        str1=""
        for L in self.Layers:
            str1+=str(L)+"\n"
        return str1

N=Network([2,10,11,3],"Neuro")
N.run([5,5])
print(N.Jacobian(2))
#N.partial(2,7,10,[0,0,0])
