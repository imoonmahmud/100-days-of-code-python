from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            random_y = randint(-300, 300)
            new_car.goto(420, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
            
