from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.position)

    def up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
