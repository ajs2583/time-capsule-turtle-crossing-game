# Time Capsule Turtle Crossing Game (Python Turtle)

This game is a simple Frogger-style crossing game built with Python’s `turtle` module. Originally created some time ago as a personal project, it is now being uploaded as a time capsule — a preserved example of my earlier programming work.

The goal of the game is to guide a turtle across a busy road full of randomly generated cars. As you progress through levels, the game gets increasingly challenging.

## Gameplay Overview

- Use the **Up Arrow** key to move the turtle forward.
- Dodge incoming cars as you cross the screen vertically.
- Each time the player reaches the finish line, the level increases and the cars speed up.
- The game ends if the turtle collides with a car.

## Technologies Used

- Python 3
- Built-in `turtle` graphics module
- Object-Oriented Programming

## File Overview

- `main.py` – Sets up the game loop, handles object coordination, and controls the game flow.
- `player.py` – Defines the player's character (turtle) and its movement.
- `car_manager.py` – Manages the creation, movement, and speed of the car obstacles.
- `scoreboard.py` – Handles level display and game over messages.
- `finish_line.py` – Draws the finish line indicator.

## How to Clone and Run

### Clone the Repository

If hosted on GitHub, clone it with:

```bash
git clone https://github.com/ajs2583/time-capsule-turtle-crossing-game.git
cd your-repo-name
