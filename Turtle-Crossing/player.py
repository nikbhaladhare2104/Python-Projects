from turtle import Turtle

STARTING = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING)

    def move(self):
        self.forward(10)

    def start(self):
        self.goto(STARTING)
