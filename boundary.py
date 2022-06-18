from turtle import Turtle


class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.speed(0)
        self.draw_boundary()

    def draw_boundary(self):
        self.penup()
        self.setposition(-299, 299)
        self.pendown()
        self.goto(-299, -299)
        self.goto(299, -299)
        self.goto(299, 299)
        self.goto(-299, 299)