import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        # missing_states = []
        # Find all the states that haven't been guessed and add them to a csv
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # If answer_state is one of the 50 states in 50_states.csv
    if answer_state in all_states:
        # if the input was correct,
        # Create a turtle to write in the x and y coordinates on the image
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv
# Generate CSV for states that have not been guessed

