# from turtle import Turtle, Screen
#
# square

# harshal = Turtle()
# harshal.shape("turtle")
# harshal.color("red")
# for i in range(4):
#     harshal.forward(100)
#     harshal.right(90)
# #
# screen = Screen()
# screen.exitonclick()

import turtle as t
import random




harshal = t.Turtle()
harshal.shape("turtle")
harshal.width(1)           # Or harshal.pensize(10)
t.colormode(255)


# Using tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

harshal.speed(0)
def draw_spirograph(x):
    for _ in range(360//x):
        harshal.color(random_color())
        harshal.circle(100)

        # CAn use this also  harshal.right(10)
        cur_heading = harshal.heading()
        harshal.setheading(cur_heading+x)


draw_spirograph(5)





#Random walk

# # colors = ["red", "blue", "green", "yellow", "violet", "indigo", "orange"]
# direction = [0,90,180,270]
# harshal.speed(0)            # can use harshal.speed("fastest")
# for i in range(200):
#     color = random_color()
#     harshal.color(color)
#     harshal.setheading(random.choice(direction))
#     harshal.forward(30)

# Drawing different shapes with different color

# for i in range(3,11):
#     harshal.color(random.choice(colors))
#     for j in range(i):
#         harshal.forward(100)
#         harshal.right(360//i)

 # Dashed line

# for i in range(15):
#     harshal.pendown()
#     harshal.forward(10)
#     harshal.penup()
#     harshal.forward(10)

# Drawing different shapes

screen = t.Screen()
screen.exitonclick()
