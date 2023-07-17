from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=1000)
screen.title("My Pong game")
screen.tracer(0)


paddle_r = Paddle((450, 0))
paddle_l = Paddle((-450, 0))
ball = Ball()
scorecard = Scorecard()


screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detecting the collision with the paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 420 or ball.distance(paddle_l) < 50 and ball.xcor() < -420:
        ball.bounce1()

    if ball.xcor() > 460:
        scorecard.l_score()
        ball.reset_position()

    if ball.xcor() < -460:
        scorecard.r_score()
        ball.reset_position()


screen.exitonclick()

# My Code
# def up_l():
#     y_cor = paddle_l.ycor() + 20
#     paddle_l.goto(paddle_l.xcor(), y_cor)
#
# def down_l():
#     y_cor = paddle_l.ycor() - 20
#     paddle_l.goto(paddle_l.xcor(), y_cor)
