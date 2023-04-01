from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []


    def car_move(self):
        for each_car in self.all_cars:
            each_car.backward(self.car_speed)


    def create_car(self):
        if random.randint(1, 6) == 1:
            self.new_car = Turtle("square")
            self.new_car.color(random.choice(COLORS))
            self.new_car.penup()
            self.new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(self.new_car)

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT
