# CS2520_MazeGame
 CS 2520 Python Project
[Map Adventure Game]
### SQUARED UP: MAZE GAME

Created by CS2520-01 Team Python

Members:
* Evelyn Vu
* Tu Nguyen
* Isabel Ganda
* Joy Sun
* Zi Guo



## DESCRIPTION OF PROJECT
We have decided to create a maze where you have to find the goal room whilst also collecting as much coins as you can get. The maze is full of intricate and confusing paths, so you might end up lost while trying to find the goal.

There will be Menu Screen at the beginning to choose options Play Game or Exit.
The game will update score point as user collect and collide with coin object.
It also loads music background which user can decide to mute by pressing key 'm'.
Watch out for Big Prize at the Win Room!

## INSTALLATION
To make this program run, you must download both Python and Pygame.

Use the following site to install [Python](https://www.python.org/downloads/)


Pygame is a set of Python modules that are utilized for creating videogames,
such as making and working with sprites, collision between items, music, and more.
follow the steps below to install Pygame:

- (For Windows) Open the command line prompt, and input the following line:
```bash
py -m pip install -U pygame --user
```

- (For Mac) Open the Terminal, and input the following line:
```bash
python3 -m pip install -U pygame --user
```

For further help with installation, use the following site for [Pygame](https://www.pygame.org/wiki/GettingStarted)

To run the game:
```bash
python main.py
```

## Getting Started
The game is simple: try to find the goal room while collecting as much coins as you can. Try to keep notes on where each path leads to where, as some paths might bring you back to where you started.

Use the key WASD:
- W - moving up
- A - moving left
- S - moving down
- D - moving right

In the first screen of the game, you will see a Menu Screen with 2 options: Start Gane or Exit (you can use mouse click to interact with the button)

- If you click Start: 
	
	- Game will start at Room 0, you can travel through the maze with different doors leading you to different rooms. There could be dead end, or some door might bring you back to where you enter. The game will end when you reach the Win Room (watch out for Big Prize ahead)

	- After the game is over, there will be two options for user to choose: Play Again or Exit
		- Choosing Play Again will restart the program and leads the user to the Menu Screen
		- Clicking Exit will terminate the program and close the window

- If you click Exit: 
	Game will terminate and close the window. 


## Controls

WASD - Move

M - Mute



