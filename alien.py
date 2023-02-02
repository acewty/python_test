import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('test/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
