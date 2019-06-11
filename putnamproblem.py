import numpy as np
import math as m
import random as r
from PIL import ImageSequence
from PIL import Image
import time
import os

def  Grey50(Base):
    avg = 0
    Grey = np.zeros((500,500))
    for i in range(500):
        for j in range(500):
            K = (Base[i,j,0]+ Base[i,j,1]+ Base[i,j,2])/3
            Grey[i,j] = K
            avg += K/(2.5*(10**5))
    #print(avg)
    Grey50x50 = np.zeros((50,50))
    for i in range(50):
        for j in range(50):
            Grey50x50[i,j] = Grey[10*i,10*j]

    BlackWhite = np.zeros((50,50))
    for i in range(50):
        for j in range(50):
            if Grey50x50[i,j] > avg :
                BlackWhite[i,j] = 1

    return BlackWhite
def screen_char(array):
    if array[0][0] == array[1][1] and (array[0][0] != array[1][0] or array[0][0] != array[0][1]):
       return "\\"
    if array[0][1] == array[1][0] and (array[0][1] != array[0][0] or array[0][1] != array[1][1]):
        return "//"
    elif array[0][0] == array[1][0] and (array[0][0] != array[0][1]):
        return "||"
    elif array[0][0] == array[0][1] and (array[0][0] != array[1][0]):
        return "--"
    else:
        return "  "
def str_sum(a):
    string = ''
    for i in a:
        string += i
    return string
def process_matrix(matrix):
    first_matrix, return_matrix = np.empty((49,49), dtype = object), np.empty((49,1), dtype = object)
    for i in range(49):
        for j in range(49):
            first_matrix[i][j] = screen_char([matrix[i:i+2][0][j:j+2],matrix[i:i+2][1][j:j+2]])
    for i in range(49):
        return_matrix[i] = str_sum(first_matrix[i])
    return return_matrix

length = 0
im = []
FullGif = []

for i in os.listdir('/Users/h205p2/Desktop/Project_Cuphead'):
    im.append(Image.open('/Users/h205p2/Desktop/Project_Cuphead/' + str(i)))
    length += 1

for Pic in im:
    Input = np.array(Pic)
    matrix_1 = Grey50(Input)
    FullGif.append(process_matrix(matrix_1))

k = 0
while True:
    print(FullGif[k])
    time.sleep(1/12)
    k += 1
    k = k % length
