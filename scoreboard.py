from turtle import Turtle

# Constant
FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"
LEVEL = "Level"
FINISH_LINE_Y = 310


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.goto(x=-235, y=360)
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)


