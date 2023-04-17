# File: game.py
# Description: A game object for the 'Jet Fighter' game. Object is used both for the server and the client.
import pygame
from constants import BACKGROUND_IMG, BLACK_PLANE_IMG, WHITE_PLANE_IMG, SCREEN_COLOR, FPS, WHITE, BLACK
from jet import Jet
import time
from tkinter import messagebox,OptionMenu,StringVar,Button,PhotoImage


class Game:
    def __init__(self, screen_width: int, screen_height: int, plane_positions: list = None):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.planes = []
        self.initialise_jets(plane_positions)
        self.score_0 = 0
        self.score_1 = 0
        self.screen = None
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.hits = []
        self.background = pygame.image.load(BACKGROUND_IMG)
        self.game_over = False

    def initialise_jets(self, positions: list = None) -> None:
        """Initialising the 'jet' objects for the game"""
        image_black = pygame.image.load(BLACK_PLANE_IMG)
        image_white = pygame.image.load(WHITE_PLANE_IMG)
        if len(self.planes) != 0:
            return
        if not positions or len(positions) < 4:
            self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
                                   plane_image=image_white, is_white=True, x=100, y=100))
            self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
                                   plane_image=image_black, is_white=False, x=500, y=500))
        else:
            if self.planes:
                self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
                                       plane_image=image_white[0], is_white=True, x=positions[0], y=positions[1]))
                self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
                                       plane_image=image_black[1], is_white=False, x=positions[2], y=positions[3]))
            else:
                self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
                                       plane_image=image_white, is_white=True, x=positions[0], y=positions[1]))
                self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
                                       plane_image=image_black, is_white=False))
        # else:
        #     self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
        #                            plane_image=image_white, is_white=True, x=positions[0], y=positions[1]))
        #     self.planes.append(Jet(screen_width=self.screen_width, screen_height=self.screen_height,
        #                            plane_image=image_black, is_white=False, x=positions[2], y=positions[3]))

    def initialise_window(self):
        """Creating initial game window"""
        messagebox.showinfo('Ready', 'Game starts in 3 seconds')
        time.sleep(3)
        screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(screen_size)
        self.screen.blit(self.background, (0, 0)) # blit the background image to the screen
        pygame.display.flip() # update the display

    def draw(self):
        """Drawing all elements on the screen"""
    
        self.screen.blit(self.background, (0, 0)) # blit the background image to the screen
        for jet in self.planes:
           jet.draw(self.screen)
        score1 = self.font.render(f"Black plane: {self.score_0}", True, (255, 0, 0) )
        score1_rect = score1.get_rect()
        score1_rect.topleft = (10, 10)
        self.screen.blit(score1, score1_rect)
        score2 = self.font.render(f"White plane: {self.score_1}", True, (255, 0, 0) )
        score2_rect = score2.get_rect()
        score2_rect.topright = (self.screen_width - 10, 10)
        self.screen.blit(score2, score2_rect)
        pygame.display.flip()
        self.clock.tick(FPS)


    def get_init_data(self):
        """Returning a dictionary with the initial game data"""
        return {'width': self.screen_width,
                'height': self.screen_height,
                'planes_pos': [self.planes[0].x, self.planes[0].y, self.planes[1].x, self.planes[1].y]}

    def update(self):
        """Updating the game"""
        for i in range(len(self.planes)):
            plane = self.planes[i]
            plane.update(self.planes[1 - i].bullets, self.hits)  # Updating each airplane

    def up_to_date_game_data(self):
        """Returning the current game data"""
        description_dict = {
            'score_0': self.score_0,
            'score_1': self.score_1,
        }
        planes = [plane.to_dict() for plane in self.planes]
        description_dict['planes'] = planes
        description_dict['game_over'] = self.game_over  # add game_over flag to game data
        return description_dict
