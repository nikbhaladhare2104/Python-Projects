from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.new_snake()
        self.head = self.turtle_list[0]

    def new_snake(self):
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        nik = Turtle()
        nik.penup()
        nik.color("white")
        nik.shape("square")
        nik.goto(position)
        self.turtle_list.append(nik)

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for i in range(len(self.turtle_list) - 1, 0, -1):
            x_cor = self.turtle_list[i - 1].xcor()
            y_cor = self.turtle_list[i - 1].ycor()
            self.turtle_list[i].goto(x_cor, y_cor)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
