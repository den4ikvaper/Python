import turtle
from turtle import Turtle, Screen, TurtleScreen
from random import randint, choice

tim = Turtle()
screen = Screen()

turtle.colormode(255)
tim.speed("fastest")


def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

step = 0

for i in range(362):
    tim.color(colors())
    tim.circle(100)
    tim.right(step)
    step =+ 1


screen.exitonclick()
