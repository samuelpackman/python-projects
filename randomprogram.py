import numpy
import math
import random
import turtle

wn=turtle.Screen()
wn.bgcolor("purple")

alex=turtle.Turtle()
alex.shape("turtle")

alex.penup()
alex.goto(0,0)
alex.pendown()
j=0
for i in range(200):
    r=random.random()
    r = r - 0.5
    r = r * 2 * math.pi
    alex.left(3*r)
    alex.forward(5)
    if j==10:
        alex.stamp()
        j=0
    else:
        j+=1
