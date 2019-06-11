import numpy as np
import PIL
from PIL import ImageSequence
from PIL import Image
import time
import os

"""typeface = input("What is your picture called? ")
img = np.array(Image.open("/Users/h205p2/Desktop/" + typeface + ".jpg"))"""

img = np.array(Image.open("/Users/h205p2/Desktop/testingimage.jpg")) #not actual code


def indpixelgrad(subarray):
    #print(subarray)
    difarray = np.zeros((3,3))
    mid = subarray[1][1]
    for c_0,i in enumerate(subarray):
        for c_1,j in enumerate(i):
            difarray[c_0,c_1]=sum(np.absolute(j-mid))
    return sum(sum(difarray))

def imgradient(array):

    return_array = np.zeros(np.array(array.shape[:2])-2*np.ones((2)).astype(int))
    for i in range(array.shape[0]-2):
        for j in range(array.shape[1]-2):
            I = indpixelgrad(array[i:i+3,j:j+3])
            if I > 1300:
                for k in range(3):
                    for l in range(3):
                        return_array[k-1,l-1] = 1300
    return return_array

gradarray = imgradient(img)
output_array = np.zeros(gradarray.shape)
im = PIL.Image.fromarray(gradarray)
im.show()
