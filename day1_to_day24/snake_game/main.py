from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

# set screen
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# even listener
screen.listen()
screen.onkey(snake.go_up, 'Up')
screen.onkey(snake.go_down, 'Down')
screen.onkey(snake.go_right, 'Right')
screen.onkey(snake.go_left, 'Left')

game_on = True
while game_on:
    screen.update()
    time.sleep(.15)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 392 or snake.head.xcor() < -400 or snake.head.ycor() > 370 or snake.head.ycor() < -395:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

    



screen.exitonclick()