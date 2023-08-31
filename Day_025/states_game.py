import turtle
import pandas

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_data = pandas.read_csv("50_states.csv")

guessed_states = []
states = state_data["state"].to_list()

score = 0

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()

# print(answer_state in states)
print(state_data[state_data["state"] == answer_state])

if answer_state in states:
    guessed_states.append(answer_state)
    state_pos = state_data[state_data["state"] == answer_state]
    x_pos = int(state_pos.x)
    y_pos = int(state_pos.y)
    # print(x_pos)
    state_title = turtle.Turtle()
    state_title.hideturtle()
    state_title.penup()
    state_title.goto(x_pos, y_pos)
    state_title.write(f"{answer_state}", align="center", font=FONT)




turtle.mainloop()
