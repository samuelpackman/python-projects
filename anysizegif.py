import numpy as np
from PIL import ImageSequence
from PIL import Image
import time
import os

def Grey50(Base):
    avg = 0
    Grey = np.zeros(np.array(Base.shape))
    for i in range(Base.shape[0]):
        for j in range(Base.shape[1]):
            K = Base[i,j]
            Grey[i,j] = K
            avg += K/(2.5*(10**5))
    #print(avg)
    Grey50x50 = np.zeros(np.array(Base.shape)//10)
    for i in range(Base.shape[0]//10):
        for j in range(Base.shape[1]//10):
            Grey50x50[i,j] = Grey[10*i,10*j]

    BlackWhite = np.zeros(np.array(Base.shape)//10)
    for i in range(Base.shape[0]//10):
        for j in range(Base.shape[1]//10):
            if Grey50x50[i,j] > avg :
                BlackWhite[i,j] = 1

    return BlackWhite

def screen_char(array):
    if array[0][0] == array[1][1] and (array[0][0] != array[1][0] or array[0][0] != array[0][1]):
       return "\\"
    if array[0][1] == array[1][0] and (array[0][1] != array[0][0] or array[0][1] != array[1][1]):
        return "//"
    if array[0][0] == array[1][0] and (array[0][0] != array[0][1]):
        return "||"
    if array[0][0] == array[0][1] and (array[0][0] != array[1][0]):
        return "--"
    return "  "
def str_sum(a):
    string = ''
    for i in a:
        string += i
    return string
def process_matrix(matrix):
    first_matrix = np.empty(np.array(matrix.shape)-np.array([1,1]), dtype = object)
    return_matrix = np.empty((matrix.shape[0]-1,1), dtype = object)
    for i in range(matrix.shape[0]-1):
        for j in range(matrix.shape[1]-1):
            first_matrix[i][j] = screen_char(matrix[i:i+2,j:j+2])
    for i in range(matrix.shape[0]-1):
        return_matrix[i] = str_sum(first_matrix[i])
    return return_matrix
input("Welcome to .ter!")
New = input("Do you want to make a new GIF or access an old one? ")
if New == "new":
    writer = input("Do you want to save your GIF?")
#    L = input("To begin, we will ask you for a GIF, is that OK?")
    #if L == "no":
        #print("That was rhetorical.")
        #time.sleep(5)
    typeface = input("What is your GIF called? ")
    img = Image.open("/Users/h205p2/Desktop/" + typeface + ".gif")
    im = [frame.copy() for frame in ImageSequence.Iterator(img)]
    length = len(im)
    FullGif = []

    print("Your GIF has " + str(length) + " frames.")
    era = float(input("How long do you want your GIF to take? (In seconds) "))

    p = 0
    for Pic in im:
        p += 1
        Input = np.array(Pic)
        print("Processing frame " + str(p) + "/" + str(length) + ".")
        matrix_1 = Grey50(Input)
        FullGif.append(process_matrix(matrix_1))

    print("GIF complete!")
    rate = era / length
    time.sleep(1)


    if writer == "yes":
        typeything = open(typeface + ".txt","w+")
        typeything.write(str(shape(FullGif[0])))
        for LINE in FullGif:
            typeything.write(str(LINE))

    k = 0
    while True:
        print(FullGif[k])
        time.sleep(rate)
        k += 1
        k = k % length

if New == "old":
    typeface = input("What is your GIF called? ")
    typeything = open(typeface + ".txt","r")
    lines = typeything.readlines()
    gif_shape = lines[0]
    print(gif_shape)
    lines = lines[1:]
    length = len(lines)//(gif_shape[0]-1)
    FullGif =[]
    for j in range(length):
        Temp = []
        for i in range(gif_shape[0]-1):
            Temp.append(lines[i + 1 + (gif_shape[0]-1) * j][1:2*gif_shape[0]+3].replace("\\\\","\\"))
        FullGif.append(Temp)
    #print(FullGif)
    FullGif = np.array(FullGif)
    #print(FullGif)
    print("Your GIF has " + str(length) + " frames.")
    era = float(input("How long do you want your GIF to take? (In seconds) "))
    rate = era / length
    k = 0
    while True:
        print(FullGif[k])
        print("\n")
        time.sleep(rate)
        k += 1
        k = k % length



else:
    print("Real funny pal. Now you just don't get a GIF.")
