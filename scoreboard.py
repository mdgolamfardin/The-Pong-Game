from turtle import Turtle  # Import the Turtle class from the turtle module

# Constants for scoreboard properties
BOARD_COLOR = 'white'  # Color of the scoreboard text

HEIGHT = 200  # Y-coordinate height where the score will be displayed
GAP = 100  # Horizontal gap between the score and the center of the screen

# Font properties
FONT_TYPE = 'Monospace'  # Font type for the scoreboard text
FONT_SIZE = 75  # Font size for the scoreboard text
FONT_STYLE = 'bold'  # Font style for the scoreboard text


class Scoreboard(Turtle):
    def write_score(self):
        """Write the current score on the screen."""
        self.write(arg=self.score, font=(FONT_TYPE, FONT_SIZE, FONT_STYLE))  # Write the score using the specified font

    def update_score(self):
        """Update the score by incrementing it and rewriting it on the screen."""
        self.score += 1  # Increment the score
        self.clear()  # Clear the previous score
        self.write_score()  # Write the updated score

    def set_location(self, side):
        """
        Set the location of the scoreboard on the screen.

        Parameters:
        side (str): The side of the screen where the scoreboard is located ('left' or 'right').
        """
        if side == 'left':
            self.goto(-GAP, HEIGHT)  # Position the scoreboard on the left side
        elif side == 'right':
            self.goto(GAP - 40, HEIGHT)  # Position the scoreboard on the right side

    def __init__(self, side):
        """
        Initialize a Scoreboard object.

        Parameters:
        side (str): The side of the screen where the scoreboard is located ('left' or 'right').
        """
        super().__init__()  # Initialize the Turtle superclass
        self.penup()  # Lift the pen to avoid drawing lines
        self.speed(0)  # Set the turtle's speed to the maximum
        self.color(BOARD_COLOR)  # Set the color of the scoreboard text
        self.score = 0  # Initialize the score to 0
        self.set_location(side)  # Set the location of the scoreboard
        self.hideturtle()  # Hide the turtle cursor
