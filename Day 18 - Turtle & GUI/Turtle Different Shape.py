from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colors = ["green", "blue", "red", "pink", "brown", "black", "grey", "purple"]


tim.speed(10)
tim.penup()
tim.backward(100)
tim.left(90)
tim.forward(200)
tim.right(90)
tim.pendown()

for i in range(3, 15):
    k = 360 / i
    tim.color(random.choice(colors))
    for j in range(i):
        tim.forward(50)
        tim.right(k)


screen = Screen()
screen.exitonclick()
