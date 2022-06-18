from turtle import Turtle
import random

coordinates = []
for i in range(-280, 300, 20):
    coordinates.append(i)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed(0)
        self.new_food()

    def new_food(self):
        self.goto(random.choice(coordinates), random.choice(coordinates))
