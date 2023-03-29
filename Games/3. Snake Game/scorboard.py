from turtle import Turtle
ALINGMENT = "center"
FONT = ('courier', 20, 'normal')


class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("YELLOW")
        self.increase_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.write(arg=f"Your Score = {self.score}", align=ALINGMENT, font=FONT)
        self.score += 1
