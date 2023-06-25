import turtle
from turtle import *
import random

turtle.colormode(255)
timmy = Turtle()
screen = Screen()
timmy.penup()
timmy.forward(100)
print(screen.canvheight)
print(screen.canvwidth)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.setposition(-300, -400)
timmy.speed(1000000000)
for i in range(10):
    x_orig=timmy.xcor()
    y_orig=timmy.ycor()
    for j in range(10):
        timmy.dot(10, color())
        timmy.goto(timmy.xcor()+50, timmy.ycor())
    timmy.setposition(x_orig,y_orig+50)

