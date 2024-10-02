from paddle import Paddle  # Import the Paddle class
from scoreboard import Scoreboard  # Import the Scoreboard class


class Player:
    def __init__(self, side):
        """
        Initialize a Player object.

        Parameters:
        side (str): The side of the screen where the player is located ('left' or 'right').
        """
        self.paddle = Paddle(side)  # Create a Paddle object for the player on the specified side
        self.scoreboard = Scoreboard(side)  # Create a Scoreboard object for the player on the specified side
