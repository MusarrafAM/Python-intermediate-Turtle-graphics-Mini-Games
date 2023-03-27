from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()


def forward():
    jim.forward(10)


def backward():
    jim.backward(10)


def turn_left():
    jim.left(10)
    # new_heading = jim.heading() + 10   This works fine as well.
    # jim.setheading(new_heading)


def turn_right():
    jim.right(10)
    # new_heading = jim.heading() - 10   This works fine as well.
    # jim.setheading(new_heading)


def undo():
    jim.undo()


def clear():
    jim.penup()
    jim.clear()
    jim.home()
    jim.pendown()


user_colour = screen.textinput(title="Etch A Sketch", prompt="Enter the colour of your sketch: ")
jim.color(user_colour)


screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=undo, key="space")
screen.onkey(fun=clear, key="c")

screen.exitonclick()

