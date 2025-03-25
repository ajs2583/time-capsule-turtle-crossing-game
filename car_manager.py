from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_START_X = 400
CAR_END_X = -300
FINISH_LINE_Y = 310


class CarManager:

    def __init__(self):
        # Creates empty list
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Creates the car and starting position
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
