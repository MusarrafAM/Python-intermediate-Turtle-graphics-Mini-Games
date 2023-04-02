from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level:{self.user_level}", font=FONT)

    def increase_score(self):
        self.clear()
        self.user_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-100, 0)
        self.write(f"GAME OVER", font=FONT)

