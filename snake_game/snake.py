from turtle import Turtle

class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.angels = {
            'up': 90,
            'down': 270,
            'left': 180,
            'right': 0
        }
        self.move_distance = 20
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position, color='white'):
        create_segment = Turtle('square')
        create_segment.color(color)
        create_segment.penup()
        create_segment.goto(position)
        self.segments.append(create_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        count = 0
        for position in self.starting_positions:
            if count == 0:
                self.add_segment(position, 'red')
            else:
                self.add_segment(position, 'white')
            count += 1

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[i-1].xcor()
            y_position = self.segments[i-1].ycor()
            self.segments[i].goto(x_position, y_position)
        self.head.forward(self.move_distance)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def go_up(self):
        if self.head.heading() != self.angels['down']:
            self.head.setheading(self.angels['up'])

    def go_down(self):
        if self.head.heading() != self.angels['up']:
            self.head.setheading(self.angels['down'])

    def go_left(self):
        if self.head.heading() != self.angels['right']:
            self.head.setheading(self.angels['left'])

    def go_right(self):
        if self.head.heading() != self.angels['left']:
            self.head.setheading(self.angels['right'])

        
