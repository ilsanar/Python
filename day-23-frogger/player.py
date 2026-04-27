from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.reposition()
        self.shape("turtle")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def reposition(self):
        self.goto(STARTING_POSITION)



