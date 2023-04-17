README file for Falcon_Multiplayer Game

Welcome to the Falcon_Multiplayer Game! This is a 2D multiplayer game where players control a Falcon jet and try to shoot down their opponents.

Getting Started:
To run the game, you need to install Python 3 and the Pygame library. Once you have these installed, you can start the game by running the server file.Now the server will wait for the connections. Since this is a multiplayer two clients can be connected using the server IP address and the port number "8200".Once the two clients get connected to the server the game starts. 

Game Controls:
Player 1: Arrow keys to move, Space bar to shoot
Player 2: Arrow keys to move, Space bar to shoot

Gameplay:
Players control their Falcon jet and try to shoot down their opponents. Players can move up, down, left, or right using the arrow keys (Player 1)  (Player 2). They can shoot bullets by pressing the space bar key (Player 1) (Player 2). The game ends when one player's scores the maximum points(5points).

Networking:
The game uses a client-server architecture to enable multiplayer gameplay. The server manages the game state and sends updates to the clients. Clients receive the game state updates and render them on the screen. The game supports LAN multiplayer.

File Structure:
The project consists of several Python files:

game.py: The main game file. This file contains the game loop and manages the interaction between the game and the player.
server.py: The server file. This file manages the game state and sends updates to the clients.
client.py: The client file. This file receives game state updates from the server and renders them on the screen.
jet.py: The jet fighter file. This file contains the Jet class, which manages the player's jet fighter.
bullet.py: The bullet file. This file contains the Bullet class, which manages the bullet objects.
ImageLabel.py: The image label file. This file contains the ImageLabel class, which supports the GIF and PNG format for displaying images.




Contributing:
If you want to contribute to the game, feel free to fork the project and submit pull requests. Contributions are welcome!


Enjoy the game!






