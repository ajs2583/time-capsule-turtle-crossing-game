import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finish_line import FinishLine

# Create instance of screen, turtle, scoreboard, finish line & cars
screen = Screen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
finish_line = FinishLine()

# Screen setup
screen.setup(width=600, height=800)

# Turns off Tracer
screen.tracer(0)


# Create Scoreboard
scoreboard.update_scoreboard()

# Key-stroke event-listener
screen.listen()
screen.onkey(player.move_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    # Update every 0.1 seconds
    time.sleep(0.1)
    screen.update()

    # Create car and start moving them
    car_manager.create_car()
    car_manager.move_cars()

    # Set up car collision with player
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.reset()
        scoreboard.next_level()
        car_manager.increase_speed()

screen.exitonclick()