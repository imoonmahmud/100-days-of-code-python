from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.R_PADDLE = (550, 0)
        self.L_PADDLE = (-550, 0)
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def position(self, side):
        if side == 'right':
            self.goto(self.R_PADDLE)
        else:
            self.goto(self.L_PADDLE)

    def go_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def go_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)
