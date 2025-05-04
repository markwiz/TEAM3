"""
Skyscraper module for the Flappy Plane game.
Handles the obstacles the player must navigate through.
"""
import pygame
import random
from constants import *

class Skyscraper:
    """
    Represents a skyscraper obstacle in the game.
    
    Creates two rectangles (top and bottom) that the player must navigate between.
    """
    
    def __init__(self, x):
        """
        Initialize a new skyscraper at the given x position.
        
        Args:
            x: The x-coordinate where the skyscraper should appear
        """
        self.height = random.randint(100,
                                     SCREEN_HEIGHT - PIPE_GAP - GROUND_HEIGHT - 100)
        self.top = pygame.Rect(x, 0, 60, self.height)
        self.bottom = pygame.Rect(x, self.height + PIPE_GAP, 60,
                                  SCREEN_HEIGHT - self.height - PIPE_GAP - GROUND_HEIGHT)
        self.passed = False
        self.color = (random.randint(50, 100), random.randint(50, 100),
                      random.randint(50, 100))

    def update(self, speed):
        """
        Updates the skyscraper's position.
        
        Args:
            speed: The speed at which the skyscraper moves left
        """
        self.top.x -= int(speed)
        self.bottom.x -= int(speed)

    def draw(self, surface):
        """
        Draws the skyscraper on the given surface.
        
        Args:
            surface: The pygame surface to draw on
        """
        pygame.draw.rect(surface, self.color, self.top)
        pygame.draw.rect(surface, (
        self.color[0] - 20, self.color[1] - 20, self.color[2] - 20), self.top,
                         2)
        pygame.draw.rect(surface, self.color, self.bottom)
        pygame.draw.rect(surface, (
        self.color[0] - 20, self.color[1] - 20, self.color[2] - 20),
                         self.bottom, 2)

    def collide(self, plane):
        """
        Checks if the plane has collided with this skyscraper.
        
        Args:
            plane: The player's plane object
            
        Returns:
            bool: True if a collision occurred, False otherwise
        """
        # Lihtsustatud kokkupõrke tuvastus
        return self.top.colliderect(plane.rect) or self.bottom.colliderect(
            plane.rect)
