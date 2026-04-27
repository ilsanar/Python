from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["yellow", "orange", "red", "green", "blue", "purple"]
user_bet = screen.textinput("Place your bet", "Which turtle will win the race. "
                                              ""f"Enter one of the colors {colors}")
turtles = []
for i in range(len(colors)):
    new_turtle = (Turtle(shape="turtle"))
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i * 30)
    turtles.append(new_turtle)

race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won, winning turtle is {winning_turtle}!")
            else:
                print(f"You lost, winning turtle is {winning_turtle}!")
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()