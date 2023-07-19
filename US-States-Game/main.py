import turtle
import pandas

screen = turtle.Screen()
screen.title("U. S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_guess = []

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States correct",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guess]
        # missing_states = []
        # for state in all_states:
        #     if state not in correct_guess:
        #         missing_states.append(state)
        break
    if answer_state in all_states:
        correct_guess.append(answer_state)
        nik = turtle.Turtle()
        nik.hideturtle()
        nik.penup()
        row = data[data.state == answer_state]
        nik.goto(int(row.x), int(row.y))
        nik.write(answer_state, align="center", font=("Ariel", 8, "bold"))
        # nik.write(row.state.item(), align="center", font=("Ariel", 8, "bold"))

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
