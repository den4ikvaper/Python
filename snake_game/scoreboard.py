from turtle import Turtle

AlIGHMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=AlIGHMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER.", align=AlIGHMENT, font=FONT)
    #
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
