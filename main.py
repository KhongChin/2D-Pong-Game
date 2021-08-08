import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
net = Net()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collisions with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_bounce()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.horizontal_bounce()

    # Detect collision with right paddle
    if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.horizontal_bounce()

    if ball.xcor() > 385:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -385:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
