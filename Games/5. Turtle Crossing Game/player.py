from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
JUMP_DISTANCE = 50


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def player_move(self):
        self.forward(MOVE_DISTANCE)

    def player_jump(self):
        self.forward(JUMP_DISTANCE)

    def is_at_finishline(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
