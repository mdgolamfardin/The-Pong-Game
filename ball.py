from turtle import Turtle  # Import the Turtle class from the turtle module
import random  # Import the random module
import math

# Constants for ball properties
BALL_COLOR = 'orange'  # Color of the ball
BALL_SIZE = 1.3  # Size of the ball
STARTING_BALL_SPEED = 10  # Speed at which the ball moves

# Constants for collision detection and ball behavior
COLLISION_DISTANCE = 20  # Distance threshold for collision detection

RESET_SLEEP = 3  # Time to sleep before resetting the ball
PADDLE_MOMENTUM = 5  # Momentum added to the ball when it hits a paddle

# Initialize starting directions for the ball
starting_directions = []
# Directions for player 2 (right side)
for i in range(0, 25):
    starting_directions.append(i)
# Directions for player 1 (left side)
for i in range(155, 205):
    starting_directions.append(i)
# Additional directions for player 2 (right side)
for i in range(335, 360):
    starting_directions.append(i)


class Ball(Turtle):
    """
    This class inherits from the Turtle class, represents a ball used in a paddle-based game (e.g., Pong). This class
    encapsulates the properties and behaviors of the ball, including its initialization, movement, collision detection,
    and interactions with paddles and walls.
    """
    def __init__(self):
        """Initialize the Ball object."""
        super().__init__("circle")  # Initialize the Turtle superclass with a circle shape
        self.color(BALL_COLOR)  # Set the ball color
        self.shapesize(BALL_SIZE)  # Set the ball size
        self.speed(0)  # Set the turtle speed to the maximum
        self.start_speed = STARTING_BALL_SPEED
        self.move_speed = self.start_speed
        self.penup()  # Lift the pen to avoid drawing lines
        self.setheading(random.choice(starting_directions))  # Set a random starting direction

    def reset(self):
        """Reset the ball to the center and set a new random direction."""
        self.goto(0, 0)  # Move the ball to the center of the screen
        self.setheading(random.choice(starting_directions))  # Set a random heading direction

    def move(self):
        """Move the ball forward."""
        self.forward(self.move_speed)  # Move the ball forward at the defined speed

    def wall_bounce(self):
        """Bounce the ball off the top or bottom wall."""
        self.setheading(360 - self.heading())  # Reflect the ball's direction vertically

    def paddle_1_bounce(self, keys):
        """Bounce the ball off player 1's paddle and adjust its direction based on paddle movement."""
        self.setheading(180 - self.heading())  # Reflect the ball's direction horizontally
        if 'w' in keys:  # If player 1 is moving the paddle up
            self.setheading(self.heading() + PADDLE_MOMENTUM)  # Adjust the heading upward
        elif 's' in keys:  # If player 1 is moving the paddle down
            self.setheading(self.heading() - PADDLE_MOMENTUM)  # Adjust the heading downward

        self.forward(STARTING_BALL_SPEED)
        self.move_speed += 1

    def paddle_2_bounce(self, keys):
        """Bounce the ball off player 2's paddle and adjust its direction based on paddle movement."""
        self.setheading(180 - self.heading())  # Reflect the ball's direction horizontally
        if 'Up' in keys:  # If player 2 is moving the paddle up
            self.setheading(self.heading() - PADDLE_MOMENTUM)  # Adjust the heading upward
        elif 'Down' in keys:  # If player 2 is moving the paddle down
            self.setheading(self.heading() + PADDLE_MOMENTUM)  # Adjust the heading downward

        self.forward(STARTING_BALL_SPEED)
        self.move_speed += 1

    def in_collision(self, paddle):
        """
        Check if the ball is in collision with a paddle.

        Parameters:
        paddle (list): A list of paddle segments.

        Returns:
        bool: True if the ball is in collision with any paddle segment, False otherwise.
        """

        # Return True if any segment is in collision distance, otherwise False

        ball_in_line = abs(self.xcor()) >= abs(paddle.xcor()) - 20
        paddle_margin = math.sqrt(math.pow(10,2) + math.pow(50, 2)) + 2
        ball_within_margin = self.distance(paddle) < paddle_margin

        collision = ball_in_line and ball_within_margin

        return collision
