from turtle import Turtle

class Scoreboard(Turtle) :


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file :
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.high_score} ", align="center", font=("Arial", 18, " normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, " normal"))

    def increase_the_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

