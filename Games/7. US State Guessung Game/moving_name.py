from turtle import Turtle


class StateName(Turtle):
    def __init__(self, state, xcor, ycor):
        super().__init__()
        self.speed("slow")
        self.penup()
        self.hideturtle()
        self.goto(xcor, ycor)
        self.write(arg=state)
