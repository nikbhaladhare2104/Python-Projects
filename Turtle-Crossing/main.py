from turtle import Screen
from player import Player
from car_manager import CarManager
from scorecard import Scorecard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scorecard = Scorecard()

screen.listen()
screen.onkey(player.move, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect collision with the upper wall
    if player.ycor() > 280:
        scorecard.increase_level()
        player.start()
        car_manager.increase_speed()

    # detect collision with the cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_on = False
            scorecard.game_over()


screen.exitonclick()
