import turtle
from guess import GuessState
from scoreboard import Scoreboard
from create_file import CreateFile

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
print(turtle.screensize()) # Printed this to find out where to place the score
# This section is to get the mouse click coordinates printed on the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
scoreboard = Scoreboard()

correct_list =[]
is_game_on = True
# missing_state = []

while len(correct_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_list)}/50", prompt="What's another states name?").title()
    user_guess = GuessState(answer_state)
    state_chosen = user_guess.get_state_matched()

    if answer_state == "Exit":
        # for item in correct_list:
        #     new_file = CreateFile(item)
        #     new_file.wrtite_to_file()
        missing_state = [state for state in user_guess.all_states() if state not in correct_list]
        # The line above replaces the 3 lines below and line 21 with list comprehension
        # for state in user_guess.all_states():
        #     if state not in correct_list:
        #         missing_state.append(state)
        print(missing_state)
        create_file = CreateFile(missing_state)
        break
    else:
        if user_guess.matched() == False:
            print("No Match")
        else:
            state_chosen_coor = user_guess.get_state_coordinates()
            user_guess.write_state()
            scoreboard.increase_level()
            correct_list.append(answer_state)
            print(correct_list)



screen.update()
#screen.exitonclick()
turtle.mainloop()
