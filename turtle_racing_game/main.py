from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []

is_race_on = False
y_position = -250
count = 0
for color in colors:
    color = Turtle(shape='turtle')
    color.shapesize(2, 2, 1)
    color.color(colors[count])
    color.penup()
    color.goto(-450, y_position)
    y_position += 100
    count += 1
    all_turtle.append(color)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 420:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color.title()} turtle is the winner! ")
            else:
                print(f"You've lost! The {wining_color.title()} turtle is the winner! ")

        random_distance = randint(0, 20)
        turtle.forward(random_distance)


screen.exitonclick()