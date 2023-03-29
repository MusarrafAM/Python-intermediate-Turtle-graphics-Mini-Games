from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.refresh()

    def refresh(self):
        food_x = random.randint(-280, 280)
        food_y = random.randint(-280, 250)
        self.goto(food_x, food_y)
