from turtle import Turtle, Screen
import random


BACKGROUND_COLOUR = "black"

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="The Turtle Race", prompt="Which turtle is going to win \nEnter the colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.bgcolor(BACKGROUND_COLOUR)

y_position = [-120, -80, -40, 0, 40, 80]
turtles = []
x_cord_end = 220  # The turtle has 40 pixels so (40/2) = 20,  250-20 = 230. I went for 220 for more accurate.
winner_colour = ""
winner = ""


# winning line
line = Turtle("turtle")
line.speed(0)
line.color("brown")
line.hideturtle()
line.penup()
line.goto(230, 150)
line.pensize(10)
line.pendown()
line.setheading(270)
line.forward(300)

for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtles.append(new_turtle)

if user_guess:
    is_game_on = Turtle

while is_game_on:
    for turtle in turtles:
        turtle.pendown()
        turtle.forward(random.randint(0, 10))
        current_x = turtle.xcor()
        if current_x >= x_cord_end:
            is_game_on = False
            winner = turtle  # to modify the turtle after game ends get that instance out.

# after win.

# message animation
message = Turtle()
message.speed(0)
message.hideturtle()
message.penup()
message.color("pink")
message.goto(-80, 150)
message.write(arg="Winner =>")

# winner animation
winner_colour = winner.pencolor()
winner.shapesize(2)  # after game fully ends  get bigger.
winner.left(450)     # after game fully ends rotate.
winner.penup()
winner.goto(x=0, y=150)

if user_guess == winner_colour:
    print("You've won !!")
else:
    print("you've lost ")
print(f"The Winner is {winner_colour}")

screen.exitonclick()


