import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        """Initalize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # loads the image of the alien ship and sets its rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # places every alien top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saves the exact position of the alien
        self.x = float(self.rect.x)