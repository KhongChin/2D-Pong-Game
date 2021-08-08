from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")
Y = 200
LEFT_X = -100
RIGHT_X = 100


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LEFT_X, Y)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_X, Y)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

