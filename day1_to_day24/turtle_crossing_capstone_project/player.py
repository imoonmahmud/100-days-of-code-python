from turtle import Turtle
STARTING_POSITION = (0, -360)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 320


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(1.5, 1.5)
        self.left(90)
        self.penup()
        self.start_position()
        

    def start_position(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


        
