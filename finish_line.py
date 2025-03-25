from turtle import Turtle

FINISH_LINE_Y = 310


class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        self.create_finish_line()

    # Draws the finish line at the finish to indicate finish
    def create_finish_line(self):
        self.hideturtle()
        self.speed("fastest")
        self.color("red")
        self.penup()
        self.goto(x=-500, y=FINISH_LINE_Y)
        self.pendown()
        self.goto(x=500, y=FINISH_LINE_Y)