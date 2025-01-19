import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S States Game')
img = './blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv('./50_states.csv')
states = data.state.to_list()
correct_states = []

while True:
    if len(correct_states) == 50:
        break

    answer = screen.textinput(title=f"{len(correct_states)}/{len(states)} Guess the State", prompt="What's another state's name?").title()
    if answer in correct_states:
        continue
    elif answer in states:
        correct_states.append(answer)
        state_data = data[data.state == answer]
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer)
        continue
    elif answer == 'Exit':
        missing_states = [state for state in states if state not in correct_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('./states_to_learn.csv')
        break
    else:
        continue

screen.exitonclick()