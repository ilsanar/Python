MOVE_DISTANCE = 10
from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(0, 2):
            self.grow((i * -10, 0))

    def grow(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def reset(self):
        for seg in self.body:
            seg.goto(1000, 1000)

        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def extend(self):
        self.grow(self.body[-1].position())

    def length(self):
        return len(self.body) - 1

    def snake_move(self):
        for seg_num in range(self.length(), 0, -1):
            self.body[seg_num].goto(self.body[seg_num - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)