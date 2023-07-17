from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "orange", "yellow", "black"]


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = 10

    def create_car(self):
        i = random.randint(1, 6)
        if i == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            ycor = random.randint(-240, 240)
            new_car.goto(300, ycor)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += 5
