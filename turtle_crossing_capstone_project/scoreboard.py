from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-380, 350)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)

