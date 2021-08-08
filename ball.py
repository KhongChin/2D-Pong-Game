from turtle import Turtle
MOVE_SPEED = 0.1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def vertical_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def horizontal_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.horizontal_bounce()
        self.move_speed = MOVE_SPEED
