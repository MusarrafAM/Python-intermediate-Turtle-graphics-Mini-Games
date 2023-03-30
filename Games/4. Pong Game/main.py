from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from  scoreboard import Scoreboard
import time


screen = Screen()

screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Split screen
screen_split = Turtle()
screen_split.hideturtle()
screen_split.pensize(10)
screen_split.color("purple")
screen_split.penup()
screen_split.goto(0, 300)
screen_split.pendown()
screen_split.right(90)

for _ in range(15):
    screen_split.forward(20)
    screen_split.penup()
    screen_split.forward(20)
    screen_split.pendown()



right_paddle = Paddle((350, 0))
right_paddle.color("red")
left_paddle = Paddle((-350, 0))
left_paddle.color("blue")

ball = Ball()
scoreboard = Scoreboard()




screen.listen()

screen.onkey(fun=right_paddle.up_fun, key="Up")
screen.onkey(fun=right_paddle.down_fun, key="Down")

screen.onkey(fun=left_paddle.up_fun, key="w")
screen.onkey(fun=left_paddle.down_fun, key="s")


game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # right Paddle misses the ball
    if ball.xcor() > 420:
        scoreboard.increase_left()
        ball.reset_ball()

    # left Paddle misses the ball
    if ball.xcor() < -420:
        scoreboard.increase_right()
        ball.reset_ball()





screen.exitonclick()