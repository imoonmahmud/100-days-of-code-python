import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)

screen.listen()
screen.onkeypress(player.go_up, 'Up')
screen.onkeyrelease(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_finish_line():
        player.start_position()
        car_manager.level_up()
        scoreboard.increase_level()
    print(car_manager.car_speed)

screen.exitonclick()