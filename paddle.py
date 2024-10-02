from turtle import Turtle  # Import the Turtle class from the turtle module

# Constants for paddle properties
LEN_STRETCH = 1
WIDTH_STRETCH = 5
PADDLE_COLOR = "white"  # Color of the paddle

# Constants for paddle positioning
LEFT_X_POS = -560  # X-coordinate for the left paddle
RIGHT_X_POS = -LEFT_X_POS  # X-coordinate for the right paddle (positive value of LEFT_X_POS)

# Constants for paddle movement and segment spacing
PART_GAP = 20  # Gap between each segment of the paddle
MOVE_SPEED = 15  # Speed at which the paddle moves


class Paddle(Turtle):
    """
    This class, which inherits from the list class, represents a paddle used in a Pong game. This class manages the
    paddle's segments, positioning, movement, and visibility.
    """
    def take_pos(self):
        """Position the paddle parts vertically in a straight line."""
        self.goto(self.xcor(), 0)

    def set_location(self, location):
        """
        Set the location of the paddle on the screen.

        Parameters:
        location (str): The side of the screen where the paddle is to be located ('left' or 'right').
        """
        if location == "left":
            x_pos = LEFT_X_POS - 10  # Adjust x-coordinate for the left paddle
            self.goto(x_pos, 0)

        elif location == "right":
            x_pos = RIGHT_X_POS + 2  # Adjust x-coordinate for the right paddle
            self.goto(x_pos, 0)

    def up(self):
        """Move the paddle up."""
        if self.ycor() < 240:  # Check if the paddle's top segment is within the screen bounds
            self.goto(self.xcor(), self.ycor() + MOVE_SPEED)  # Move each part up

    def down(self):
        """Move the paddle down."""
        if self.ycor() > -230:  # Check if the paddle's bottom segment is within the screen bounds
            self.goto(self.xcor(), self.ycor() - MOVE_SPEED)  # Move each part down

    def __init__(self, side):
        """
        Initialize the Paddle object.

        Parameters:
        side (str): The side of the screen where the paddle is located ('left' or 'right').
        """
        super().__init__("square")  # Initialize the list superclass
        self.shapesize(stretch_wid=WIDTH_STRETCH, stretch_len=LEN_STRETCH)
        self.color(PADDLE_COLOR)
        self.penup()
        self.set_location(side)  # Set the location of the paddle
