# The Pong Game

This repository contains the Python code for a simple implementation of the classic arcade game "Pong." Building this game is a part of an educational course on Python programming from Udemy.

## Files

The software is divided into several Python files, each handling a specific aspect of the game:

- `main.py`: This is the main driver script that initializes the game window and controls the game loop.
- `ball.py`: Manages the properties and movements of the pong ball.
- `paddle.py`: Defines the paddle's behavior, including its creation and movement mechanics.
- `player.py`: Handles player-related information, primarily for managing multiple players in the game.
- `scoreboard.py`: Responsible for displaying and updating the game's scoreboard.

## Technologies Used

This Pong game is implemented using Python 3. Here are some of the key technologies and libraries used in the development of this game:

- **Python 3:** The core language used for the entire game logic and structure.
- **Turtle Graphics:** A standard Python library used for creating the game window, drawing the game elements like paddles and ball, and handling the animation.
- **Git:** Used for version control to manage the changes and collaboration throughout the development of the game.

## Installation

To run this game, you will need Python installed on your system. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/The-Pong-Game.git
```

Navigate to the cloned directory:
```bash
cd The-Pong-Game
```

Run the game using Python:
```bash
python main.py
```

### Alternative Installation (Without Terminal/Command Lines)
1. Download the zip file from [here](https://github.com/mdgolamfardin/The-Pong-Game).
2. Run `main.py` using an IDE (PyCharm for example). Install an IDE if you don't have one already.

## Gameplay

To play the game, launch `main.py`. Control the left paddle with the 'W' and 'S' keys for up and down movements, respectively. Control the right paddle using the 'Up Arrow' and 'Down Arrow' keys.

The ball will bounce off the paddles, and the walls upward and downward. If one player misses the ball, the other player scores a point.

The game continues until one player reaches a score of 10. The scoreboard at the top will update in real-time as players score points.

## Contributing

Contributions to this project are welcome, especially from fellow learners who are also taking the Udemy Python course. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b improve-feature`).
3. Make the appropriate changes in the files.
4. Commit your changes (`git commit -am 'Add some improvements'`).
5. Push to the branch (`git push origin improve-feature`).
6. Create a pull request.
## Acknowledgments

This project is a part of the course "100 Days of Code: The Complete Python Pro Bootcamp", taught by Dr. Angela Yu on Udemy.
## Author
- [mdgolamfardin](https://github.com/mdgolamfardin)
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
Enjoy playing Pong, and happy coding!
