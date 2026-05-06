from time import sleep
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

table = Screen()
table.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
table.bgcolor("black")
table.title("Pong")
table.tracer(0)

paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

table.listen()
table.onkey(key="Up", fun=paddle_right.move_up)
table.onkey(key="Down", fun=paddle_right.move_down)

table.onkey(key="w", fun=paddle_left.move_up)
table.onkey(key="s", fun=paddle_left.move_down)

game_is_on = True
while game_is_on:
    table.update()
    sleep(1 / 30)
    ball.move()
    if ball.ycor() >= int(SCREEN_HEIGHT / 2 - 20) or ball.ycor() <= int(SCREEN_HEIGHT / -2 + 20):
        ball.bounce_wall()

    if (ball.xcor() >= paddle_right.xcor() - 20 and ball.distance(paddle_right) < 50
            or ball.xcor() <= paddle_left.xcor() + 20 and ball.distance(paddle_left) < 50):
        ball.bounce_paddle()

    if ball.xcor() > 380:
        scoreboard.point_l()
        ball.new_ball(ball.xcor())
        table.update()
        sleep(2)

    if ball.xcor() < -380:
        scoreboard.point_r()
        ball.new_ball(ball.xcor())
        table.update()
        sleep(2)

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False
        scoreboard.game_over()

table.exitonclick()


