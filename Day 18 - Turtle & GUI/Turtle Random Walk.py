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



########################################## Angela Yu code ##########################################
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))

