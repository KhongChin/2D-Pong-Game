from turtle import Turtle
DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def up(self):
        self.forward(DISTANCE)

    def down(self):
        self.back(DISTANCE)

