"""
Ground module for the Flappy Plane game.
Implements the game's ground/terrain.
"""
import pygame
from constants import *

class Ground:
    """
    Represents the ground at the bottom of the game screen.
    
    The ground acts as both a visual element and a collision surface.
    """
    
    def __init__(self):
        """
        Initialize the ground with its position and appearance.
        """
        self.image = pygame.Surface((SCREEN_WIDTH, GROUND_HEIGHT))
        self.image.fill(ORANGE)
        # Joonista muru
        for i in range(0, SCREEN_WIDTH, 5):
            pygame.draw.rect(self.image, (0, 100, 0), (i, 0, 5, 10))
        self.rect = self.image.get_rect(
            topleft=(0, SCREEN_HEIGHT - GROUND_HEIGHT))

    def update(self):
        """
        Updates the ground's state.
        This method exists for consistency with other game objects.
        """
        pass

    def draw(self, surface):
        """
        Draws the ground on the given surface.
        
        Args:
            surface: The pygame surface to draw on
        """
        surface.blit(self.image, self.rect)
