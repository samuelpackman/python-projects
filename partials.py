import numpy as np



def Jacobian(self,n,nodes): #collumns are df_i for every i, rows for dx_j for every j every f_i included in each collumn
    input_dim = len(self.Layers[n]) # i is index of input node, j is index of output node
    output_dim= len(self.Layers[n+1])    #outputmatrix = np.zeros((inputdim,output_dim))  #not actually used just notes
    Jacobian_weights =  np.array([self.Layer[n].weights[i:j] for i range(input_dim)] for j in range(output_dim)])   # stacked matrix of all of the weights in each row
    Jacobian_sigmoids = []   #stacked matrix of all the sigmoid_primes in each collumn
    sigmoid_collumn = []
    for j in range(output_dim):
        sigmoid_collumn += [[]]




f:R^n -> R^m
J_f(x)_i,j
=df_i/dx_j


print(np.zeros((4)))
