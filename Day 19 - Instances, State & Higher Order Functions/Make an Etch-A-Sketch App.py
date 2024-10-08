from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(5)


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def turn_left():
    tim.right(10)
    tim.forward(20)


def turn_right():
    tim.left(10)
    tim.forward(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")


screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=turn_left)
screen.onkey(key="D", fun=turn_right)

screen.exitonclick()
