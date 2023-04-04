import turtle
from moving_name import StateName
import pandas

already_guessed = []

screen = turtle.Screen()
screen.title("Us state project")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()  # Add the list of states

score = 0
while len(already_guessed) < 50:
    user_guess = screen.textinput(title=f"{score}/50 states correct", prompt="Guess another state name").title()
    if user_guess == "Exit":
        # missing_states = []
        # for state in states:
        #     if state not in already_guessed:
        #         missing_states.append(state)
        missing_states = [state for state in states if state not in already_guessed]  # This is listComprehension cont:
        # This one line of listComprehension will do the above 4 lines of code(commended)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_guess in already_guessed:
        print("already guessed")
    elif user_guess in states:
        print(f"{user_guess} is Correct")
        score += 1
        already_guessed.append(user_guess)
        states_data = data[data.state == user_guess]

        x_cor = states_data.x.item()  # This .item() will get the first element of the pandas dataframe.
        y_cor = states_data.y.item()
        new_city = StateName(user_guess, x_cor, y_cor)



