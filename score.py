from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.hideturtle()
        self.draw_score()

    def increase(self):
        self.score += 1
        self.draw_score()

    def draw_score(self):
        self.setposition(0, 301)
        self.clear()
        self.write("Score: " + str(self.score), align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER!", align="center", font=('Arial', 20, 'normal'))

