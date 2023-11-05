########################################## My code ##########################################
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colors = ["green", "blue", "red", "pink", "brown", "black", "grey", "purple"]
direction = [0, 1, 2]

tim.speed(10)
tim.width(10)

for i in range(200):
    tim.forward(20)
    ran = random.choice(direction)
    tim.color(random.choice(colors))
    if ran == 0:
        tim.forward(20)
    elif ran == 1: 
        tim.right(90)
    else:
        tim.left(90)
        

screen = Screen()
screen.exitonclick()
