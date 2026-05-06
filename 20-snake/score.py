from turtle import Turtle

ALIGNMENT = "Center"
FONT = ('Arial', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setpos(0, 275)
        self.points = 0
        self.high_score = 0
        self.get_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.points} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.points += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.write_high_score()
        self.update_score()

    def get_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def write_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
