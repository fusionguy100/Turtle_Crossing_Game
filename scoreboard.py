from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color('Black')
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f"Level: {self.level}", align= "Left", font = FONT)

