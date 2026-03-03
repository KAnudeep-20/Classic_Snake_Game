from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        #Here,  we the below because we vs code cannot directly use it from the main game file so use this path
        file_path = os.path.join(os.path.dirname(__file__), "data.txt")
        with open(file_path) as hs:
            self.highscore = int(hs.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 22, "normal"))

    def reset(self):
        if(self.score>self.highscore):
            self.highscore = self.score
            #Here, it will write the high score of the game in the file to a new high score
            file_path = os.path.join(os.path.dirname(__file__), "data.txt")
            with open(file_path, mode='w') as hs:
                hs.write(f"{self.highscore}")
        self.score = 0
        self.increase_score()
