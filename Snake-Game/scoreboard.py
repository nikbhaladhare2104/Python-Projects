from turtle import Turtle
FONT = ("Ariel", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("/Users/nikhilbhaladhare/Desktop/data.txt") as data:
            self.high = int(data.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.scorecard()

    def scorecard(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"Score : {self.score}  High Score: {self.high}", align="center", font=FONT)

    def final_scorecard(self):
        self.clear()
        if self.score > self.high:
            self.high = self.score
            with open("/Users/nikhilbhaladhare/Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high}")
        self.goto(0, 275)
        self.write(f"Score : {self.score}  High Score: {self.high}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.scorecard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! ", align="center", font=FONT)
