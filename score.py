from turtle import Turtle


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=self.score, font=("courier", 100, "bold"))

    def increase_score(self):
        self.score += 1
        self.display_score()
