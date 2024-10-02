# Required Imports
from turtle import Screen, Turtle

from ball import Ball  # Assuming this file defines the Ball class
from player import Player  # Assuming this file defines the Player class
import time

# Screen and Game Setup
SCREEN_SIZE = (1200, 600)  # Width and height of the game screen
SCREEN_COLOR = 'black'  # Background color of the screen
SCREEN_BOUNDARY_Y = (SCREEN_SIZE[1] / 2) - 10  # Upper wall for the ball
SCREEN_BOUNDARY_Y_NEG = -((SCREEN_SIZE[1] / 2) - 18)  # Lower wall for the ball
SCREEN_BOUNDARY_X = (SCREEN_SIZE[0] / 2) - 1  # Player 1 scoreline
SCREEN_BOUNDARY_X_NEG = -((SCREEN_SIZE[0] / 2) + 2)  # Player 2 scoreline

STRETCH = 40  # Stretch needed paddle's x-coordinate to equal goal boundary

PITCH_LINE_GAP = 15  # Spacing between dashes on the center line
PITCH_LINE_WIDTH = 6  # Thickness of the center line
PITCH_LINE_COLOR = "white"  # Color of the center line

WINNING_SCORE = 10  # Number of points needed to win the game

INTRO_PAUSE = 3  # (seconds) Initial pause before the game starts

# Initialize Screen
screen = Screen()
screen.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])  # Set screen size
screen.tracer(0)  # Turn off automatic screen update for smoother performance
screen.title("Pong")  # Title of the game on window

# Turtle to draw center line
line = Turtle()

# Create Players
player_1 = Player('left')  # Player on the left side
player_2 = Player('right')  # Player on the right side

# Create Ball
ball = Ball()

# Track Key Presses
pressed_keys = []  # List to store currently pressed keys


# Functions for Drawing the Center Line
def draw_line():
    """
    Draws the center line on the screen.
    """
    screen.tracer(0)  # Turn off update to prevent flicker
    line.hideturtle()  # Hide the turtle object
    line.color(PITCH_LINE_COLOR)
    line.speed(0)  # Set drawing speed to fastest
    line.width(PITCH_LINE_WIDTH)  # Set line thickness
    line.penup()  # Don't draw until positioned
    starting_y_pos = (SCREEN_SIZE[1] / 2) - PITCH_LINE_GAP  # Calculate starting y position
    line.goto(0, starting_y_pos)  # Move to starting position

    for i in range(int(starting_y_pos), (int(starting_y_pos) * -1) + PITCH_LINE_GAP, -PITCH_LINE_GAP):
        """
        Loop to draw the center line with gaps
        """
        line.pendown()  # Start drawing
        if i % (PITCH_LINE_GAP * 2) == 0:  # Check if gap position
            line.penup()  # Skip a segment for the gap
        line.setheading(270)  # Set direction to draw vertically
        line.forward(PITCH_LINE_GAP)  # Move forward to draw line segment

    screen.update()  # Update the screen after drawing


# Functions for Tracking Key Presses
def add_w():
    """
    Adds 'w' to the pressed_keys list for player 1 movement.
    """
    pressed_keys.append('w')


def add_s():
    """
    Adds 's' to the pressed_keys list for player 1 movement.
    """
    pressed_keys.append('s')


def add_up():
    """
    Adds 'Up' to the pressed_keys list for player 2 movement.
    """
    pressed_keys.append('Up')


def add_down():
    """
    Adds 'Down' to the pressed_keys list for player 2 movement.
    """
    pressed_keys.append('Down')


def rem_w():
    """
    Removes 'w' from the pressed_keys list for player 1 movement.
    """
    pressed_keys.remove('w')


def rem_s():
    """
    Removes 's' from the pressed_keys list for player 1 movement.
    """
    pressed_keys.remove('s')


def rem_up():
    """
    Removes 'Up' from the pressed_keys list for player 2 movement.
    """
    pressed_keys.remove('Up')


def rem_down():
    """
    Removes 'Down' from the pressed_keys list for player 2 movement.
    """
    pressed_keys.remove('Down')


def reset():
    """
    Resets the ball and player positions to the starting positions,
    clears the score and prepares for a new round.
    """
    ball.reset()  # Calls a method on the Ball object to reset its position
    ball.move_speed = ball.start_speed
    player_1.paddle.take_pos()  # Calls a method on Player 1's paddle to reset its position
    player_2.paddle.take_pos()  # Calls a method on Player 2's paddle to reset its position


def goal(player):
    """
    Handles a goal scored by a player

    - Updates the player's score.
    - Displays a short pause on the screen.
    - Checks if the winning score is reached.
        - If yes, displays a game over message for the winning player and exits the loop.
    - Resets the game (clears score and positions).
    - Displays a short pause on the screen.
    - Returns True to keep the game loop running.
    """
    player.scoreboard.update_score()  # Update the player's score
    screen.update()  # Update the screen to reflect the score change
    time.sleep(1)  # Pause the game for 1 second

    if player_1.scoreboard.score == WINNING_SCORE:
        game_over("Player 1 Won")
        return False  # Exit the game loop if Player 1 wins
    elif player_2.scoreboard.score == WINNING_SCORE:
        game_over("Player 2 Won")
        return False  # Exit the game loop if Player 2 wins

    reset()  # Reset the game for the next round
    screen.update()  # Update the screen to reflect the reset
    time.sleep(1)  # Pause the game for 1 second

    return True  # Continue the game loop


def game_over(message):
    """
    Displays a game over screen with the winning message
    and instructions to restart the game
    """

    # Restart the game when the space bar is pressed
    screen.onkey(key='space', fun=play)

    line.clear()  # Clear the center line
    player_1.scoreboard.score = 0  # Reset player 1 score
    player_2.scoreboard.score = 0  # Reset player 2 score
    player_1.scoreboard.clear()  # Clear the scoreboard display for player 1
    player_2.scoreboard.clear()  # Clear the scoreboard display for player 2
    player_1.paddle.hideturtle()  # Hide player 1's paddle
    player_2.paddle.hideturtle()  # Hide player 2's paddle
    ball.hideturtle()  # Hide the ball

    line.penup()  # For pen to move the turtle without drawing
    line.goto(-180, (SCREEN_SIZE[1] / 2) / 3)  # Move the turtle to a specific position

    # Write the game over message in a large bold font
    line.write(arg=message, font=("Arial", 60, 'bold'))

    line.goto(-140, -((SCREEN_SIZE[1] / 2) / 3))  # Move the turtle to another position

    # Write instructions to restart the game in a smaller font
    line.color('light green')  # Set the text color to light green
    line.write(arg="Press Space for a rematch!", font=("Arial", 25, 'normal'))

    screen.update()  # Update the screen to show the game over message


def play():
    """Initialize and start the game."""
    line.clear()  # Clear the line drawn on the screen
    reset()  # Reset the game state
    player_1.paddle.showturtle()  # Show player 1's paddle
    player_2.paddle.showturtle()  # Show player 2's paddle
    player_1.scoreboard.write_score()  # Display player 1's score
    player_2.scoreboard.write_score()  # Display player 2's score
    ball.showturtle()  # Show the ball
    screen.bgcolor(SCREEN_COLOR)  # Set the background color of the screen
    draw_line()  # Draw the center line

    screen.update()  # Update the screen to reflect changes

    # Set up key bindings for player controls
    screen.onkeypress(key='w', fun=add_w)  # Move player 1's paddle up
    screen.onkeypress(key='s', fun=add_s)  # Move player 1's paddle down
    screen.onkeypress(key='Up', fun=add_up)  # Move player 2's paddle up
    screen.onkeypress(key='Down', fun=add_down)  # Move player 2's paddle down

    screen.onkeyrelease(key="w", fun=rem_w)  # Stop moving player 1's paddle up
    screen.onkeyrelease(key="s", fun=rem_s)  # Stop moving player 1's paddle down
    screen.onkeyrelease(key="Up", fun=rem_up)  # Stop moving player 2's paddle up
    screen.onkeyrelease(key="Down", fun=rem_down)  # Stop moving player 2's paddle down

    screen.listen()  # Listen for key presses

    game_on = True  # Set the game state to active
    time.sleep(3)  # Wait for 3 seconds before starting the game loop
    while game_on:
        if 'w' in pressed_keys:  # If 'w' is pressed, move player 1's paddle up
            player_1.paddle.up()
        elif 's' in pressed_keys:  # If 's' is pressed, move player 1's paddle down
            player_1.paddle.down()

        if 'Up' in pressed_keys:  # If 'Up' is pressed, move player 2's paddle up
            player_2.paddle.up()
        elif 'Down' in pressed_keys:  # If 'Down' is pressed, move player 2's paddle down
            player_2.paddle.down()

        ball.move()  # Move the ball

        # Check for ball collision with the top or bottom wall
        if ball.ycor() >= SCREEN_BOUNDARY_Y or ball.ycor() <= SCREEN_BOUNDARY_Y_NEG:
            ball.wall_bounce()  # Bounce the ball off the wall

        # Check for ball collision with player 1's paddle
        if ball.in_collision(player_1.paddle):
            ball.paddle_1_bounce(pressed_keys)  # Bounce the ball off player 1's paddle
        # Check for ball collision with player 2's paddle
        elif ball.in_collision(player_2.paddle):
            ball.paddle_2_bounce(pressed_keys)  # Bounce the ball off player 2's paddle

        # Check if player 1 scores
        if ball.xcor() > SCREEN_BOUNDARY_X:
            game_on = goal(player_1)  # Update score and game state
        # Check if player 2 scores
        elif ball.xcor() < SCREEN_BOUNDARY_X_NEG:
            game_on = goal(player_2)  # Update score and game state

        screen.update()  # Update the screen to reflect changes


play()  # Start the game

screen.exitonclick()  # Keep the window open until it is clicked
