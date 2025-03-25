from turtle import Turtle

# Constants
STARTING_POSITION = (0, -350)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset()

    # Moves the player up
    def move_up(self):
        # Takes the turtles current y coordinates and then adds MOVE_DISTANCE to it
        self.forward(MOVE_DISTANCE)



    def is_at_finish_line(self):
        # If player reaches Finish Line, reset the position of the turtle
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # Resets turtle position
    def reset(self):
        self.goto(STARTING_POSITION)


