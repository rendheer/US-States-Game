import pandas
from turtle import Turtle

class CreateFile(Turtle):
    def __init__(self, list):
        super().__init__()
        self.states_to_learn = list
        # self.states_to_learn.append(list)
        self.wrtite_to_file()

    def wrtite_to_file(self):
        df = pandas.DataFrame(self.states_to_learn)
        file_name = "states_to_learn.csv"
        print(self.states_to_learn)
        df.to_csv(file_name)
