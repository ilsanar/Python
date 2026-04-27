from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [(310, -235), (310, -205), (310, -175), (310, -145), (310, -115), (310, -85), (310, -55), (310, -25), (310, 5),
         (310, 35), (310, 65), (310, 95), (310, 125), (310, 155), (310, 185), (310, 215), (310, 245)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FIRST_LANE = -250


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        lane_ycor = FIRST_LANE
        super().__init__()
        self.hideturtle()
        self.pencolor("grey")
        self.penup()
        self.goto(-300, lane_ycor)
        while self.ycor() <= 260:
            while self.xcor() <= 300:
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)
            self.penup()
            lane_ycor += 30
            self.goto(-300, lane_ycor)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(random.choice(LANES))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def delete_cars(self):
        for car in self.all_cars:
            if car.xcor() < -330:
                c = self.all_cars.pop(self.all_cars.index(car))
                c.hideturtle()
                c.clear()
                del c

    def speed_up(self):
        self.speed += MOVE_INCREMENT




