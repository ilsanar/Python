from turtle import Turtle, Screen
from random import *




def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b



tim = Turtle()
screen = Screen()
screen.screensize(300, 300)
screen.colormode(255)
tim.speed(0)

colors_rgb = [(214, 154, 105), (49, 96, 139), (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25),
              (120, 163, 202), (56, 30, 18), (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160),
              (162, 20, 10), (125, 181, 156), (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113),
              (48, 170, 98), (39, 62, 97), (27, 91, 52), (235, 162, 187), (108, 118, 172), (225, 206, 2),
              (6, 88, 108), (227, 179, 170), (65, 81, 31), (140, 214, 195), (170, 183, 217), (54, 146, 192),
              (165, 203, 213)]

tim.penup()
tim.hideturtle()
tim.teleport(-250, -250)

for i in range(10):
    for _ in range(10):
        color = choice(colors_rgb)
        tim.dot(20, color)
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    if tim.position()[0] > 0:
        tim.setheading(180)
    else:
        tim.setheading(0)
    tim.forward(50)

screen.exitonclick()