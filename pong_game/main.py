from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

r_paddle = Paddle()
r_paddle.position('right')
l_paddle = Paddle()
l_paddle.position('left')

ball = Ball()
scoreboard = Scoreboard()

paddle = Turtle()
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

screen.onkeyrelease(r_paddle.go_up, 'Up')
screen.onkeyrelease(r_paddle.go_down, 'Down')
screen.onkeyrelease(l_paddle.go_up, 'w')
screen.onkeyrelease(l_paddle.go_down, 's')

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 375 or ball.ycor() < -375:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 510 or ball.distance(l_paddle) < 50 and ball.xcor() < -510:
        ball.bounce_x()

    # Detect r paddle misses
    if ball.xcor() > 600:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l paddle misses
    if ball.xcor() < -600:
        ball.reset_position()
        scoreboard.r_point()
        

    


screen.exitonclick()

