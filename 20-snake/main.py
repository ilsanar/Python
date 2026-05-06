from time import sleep
from turtle import Screen

from score import Score
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="w", fun=snake.go_up)
screen.onkey(key="s", fun=snake.go_down)
screen.onkey(key="a", fun=snake.go_left)
screen.onkey(key="d", fun=snake.go_right)
game_on = True

while game_on:
    screen.update()
    sleep(1 / 20)
    snake.snake_move()

    #Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_point()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()
screen.exitonclick()


