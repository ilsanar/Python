from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.draw_net()
        self.goto(x=100, y=200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=-100, y=200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def point_r(self):
        self.r_score += 1
        self.update()

    def point_l(self):
        self.l_score += 1
        self.update()

    def draw_net(self):
        self.teleport(x=0, y=-300)
        self.setheading(90)
        self.pensize(5)
        while self.ycor() < 320:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        if self.l_score > self.r_score:
            self.write("Left Won!", align="center", font=("Courier", 80, "normal"))
        else:
            self.write("Right Won!", align="center", font=("Courier", 80, "normal"))