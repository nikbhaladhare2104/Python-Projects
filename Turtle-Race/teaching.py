import turtle
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
tim.shapesize(5)


def move_forwards():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    curr_head = tim.heading()
    tim.setheading(curr_head + 10)


def clockwise():
    curr_head = tim.heading()
    tim.setheading(curr_head - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

    
screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

# screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
