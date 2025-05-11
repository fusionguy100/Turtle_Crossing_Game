from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('Black')
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f"Level: {self.level}", align= "Left", font = FONT)

    def scoreboard_update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=FONT)


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! You got to level {self.level}", align="Center", font=FONT)
