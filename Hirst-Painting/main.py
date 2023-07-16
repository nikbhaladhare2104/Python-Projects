import colorgram
import random
import turtle as t
# Extracting the color pallet from the image to make hirst painting

# colors = colorgram.extract("img.jpg", 30)
# rgb=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
# print(rgb)


color_list = [(240, 231, 56), (221, 154, 74), (185, 64, 30), (239, 42, 120), (191, 12, 32), (35, 96, 173), (45, 213, 79), (20, 24, 54), (37, 35, 156), (234, 228, 4), (87, 185, 220), (220, 163, 10), (205, 12, 6), (196, 37, 78), (49, 25, 15), (74, 12, 47), (233, 58, 37), (26, 144, 31), (84, 236, 176), (80, 211, 144), (219, 138, 183), (12, 200, 218), (95, 75, 12), (241, 157, 197), (75, 80, 217), (11, 36, 28)]
nik = t.Turtle()
t.colormode(255)
nik.speed(0)
nik.hideturtle()
nik.penup()
nik.setheading(225)
#nik.penup()
nik.forward(300)
nik.setheading(0)

for _ in range(10):
    #nik.setposition(0,i)
    for _ in range(10):
        nik.color(random.choice(color_list))
        nik.dot(20)
        nik.forward(50)

    nik.setheading(90)
    nik.forward(50)
    nik.setheading(180)
    nik.forward(500)
    nik.setheading(0)



screen = t.Screen()
screen.exitonclick()