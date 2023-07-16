from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=500)

user_bet = screen.textinput(title="Turtle race", prompt="Which one are you betting on?:")
color_list = ["red", "blue", "green", "yellow", "orange", "black"]
turtle_list = []

y_position = [-120, -70, -20, 30, 80, 130]

for i in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[i])
    new_turtle.goto(x=-230, y=y_position[i])
    turtle_list.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for item in turtle_list:
        if item.xcor() > 230:
            race_on = False
            item_color = item.pencolor()
            if user_bet == item_color:
                print(f"You've won! The {item_color} is the winner.")
            else:
                print(f"You've lost! The {item_color} is the winner.")

        speed = random.randint(1, 10)
        item.forward(speed)


screen.exitonclick()
