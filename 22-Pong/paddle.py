from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.move_to_start_position(x, y)

    def move_to_start_position(self, posx, posy):
        self.teleport(posx, posy)

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(40)
