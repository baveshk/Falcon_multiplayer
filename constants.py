# File: constants.py
# Description: Constants for the 'Jet Fighter' game.
import os
import pygame
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
BLACK_PLANE_IMG = os.path.join('images', 'new_jet1.png')
WHITE_PLANE_IMG = os.path.join('images', 'image.png')
LOADING_IMG = os.path.join('images', 'loading.gif')
BACKGROUND_IMG = os.path.join('images', 'background.png')
BACKGROUND_IMG1 = os.path.join('images', 'bm.PNG')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


SERVER_LISTEN_IP = "0.0.0.0"
SERVER_IP = "192.168.1.197"

SERVER_PORT = 8200

ROTATE_AMOUNT = 2.5

FPS = 20
SCREEN_COLOR = (130, 130, 130)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WHITE_CONTROLS = [pygame.K_LEFT, pygame.K_RIGHT]
BLACK_CONTROLS = [pygame.K_a, pygame.K_d]
