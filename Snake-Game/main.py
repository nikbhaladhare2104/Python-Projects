from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with the walls
    if snake.head.xcor() > 275 or snake.head.ycor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() < -275:
        scoreboard.game_over()
        scoreboard.final_scorecard()
        game_on = False

    # detect collision with its own tail
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            scoreboard.final_scorecard()
            game_on = False

    snake.move()
screen.exitonclick()
