import pandas
from turtle import Turtle
FONT = ("Courier", 8, "normal")

class GuessState(Turtle):
    def __init__(self, user_state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.user_state = user_state
        self.data = pandas.read_csv("50_states.csv")
        # self.get_state_matched()
        self.state_from_file = ""
        self.guessed_states = []


    def get_state_matched(self):
        self.state = self.data[self.data["state"] == self.user_state]
        print(f"Matched {self.state.state}")
        self.state_from_file = self.state.state
        print(f"State matched: {len(self.state_from_file)}")
        # if len(self.state_from_file) > 0:
        #     self.guessed_states.append(self.user_state)
        # # self.guessed_states.append(self.state_from_file)
        # print(f"The guessed states are {self.guessed_states}")
        return self.state_from_file

    def get_state_coordinates(self):
        user_state_x = self.state.x
        user_state_y = self.state.y
        print(f"State x is : {len(user_state_x)}")
        state_coor = (int(user_state_x), int(user_state_y))
        print(state_coor)
        self.goto(state_coor)
        return state_coor

    def write_state(self):
        self.goto(self.get_state_coordinates())
        self.write(self.user_state, align="center", font=FONT)

    def matched(self):
        if len(self.state_from_file) == 0:
            print("Invalid State")
            return False
        else:
            print(self.state_from_file)
            return True

    def all_states(self):
        self.all_state_list = self.data["state"].to_list()
        return self.all_state_list