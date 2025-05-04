"""
Cloud module for the Flappy Plane game.
Implements decorative background elements.
"""
import pygame
import random
from constants import *

class Cloud:
    """
    Represents a decorative cloud in the background.
    
    Clouds move at different speeds to create a parallax effect.
    """
    
    def __init__(self):
        """
        Initialize a new cloud with random position, size and speed.
        """
        self.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.y = random.randint(0, SCREEN_HEIGHT // 2)
        self.speed = random.uniform(0.5, 1.5)
        self.size = random.randint(20, 50)

    def update(self):
        """
        Updates the cloud's position.
        
        Returns:
            bool: True if the cloud has moved off-screen, False otherwise
        """
        self.x -= self.speed
        return self.x + self.size < 0

    def draw(self, surface):
        """
        Draws the cloud on the given surface.
        
        Args:
            surface: The pygame surface to draw on
        """
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)),
                           self.size)
