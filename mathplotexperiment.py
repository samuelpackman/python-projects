import turtle
import math

wn=turtle.Screen()
wn.bgcolor("lightblue")

alex = turtle.Turtle()

def f(x):
    return math.sin(x/50)*50

alex.penup()
alex.goto(-300,f(-300))
alex.pendown()



for i in range(-300,301):
    alex.goto(i,f(i))

wn.exitonclick()
