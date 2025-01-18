from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        x = randint(-350, 350)
        y = randint(-350, 350)
        self.goto(x, y)
