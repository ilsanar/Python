import turtle, pandas as pd


class StateWriter(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()


# def get_mouse_click_cor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_cor)


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
name_writer = StateWriter()

score = 0
title = "Name all U.S states"
data = pd.read_csv("./50_states.csv")
states_list = data.state.to_list()
# print(states_list)


while score < 50:
    answer = screen.textinput(title, "What's a state name").title()

    if answer == "Exit":
        output_data = pd.DataFrame({"Missed States": states_list})
        output_data.to_csv("./Missed_states.csv")
        break
    elif answer in states_list:
        selected_state = data[data.state == answer]
        name_writer.teleport(selected_state.x.item(), selected_state.y.item())
        name_writer.write(answer)
        score += 1
        title = f"{score}/50 States Correct"
        states_list.remove(answer)

name_writer.goto(0, 400)
name_writer.write("Congratulations! You got them all!", align="center", font=("Arial", 20, "bold"))

screen.mainloop()

