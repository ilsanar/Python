from turtle import Turtle


BALL_SPEED = 5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1.1
        self.y_move *= 1.1

    def new_ball(self, position):
        dir_modifier = 1
        if position > 0:
            dir_modifier = -1
        self.goto(0, 0)
        self.x_move = BALL_SPEED * dir_modifier
        self.y_move = BALL_SPEED




