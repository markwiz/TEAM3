"""
Plane module for the Flappy Plane game.
Handles the player-controlled airplane.
"""
import pygame
import math
from constants import *

class Plane:
    """
    Represents the player-controlled airplane.
    
    Handles plane movement, physics, animation, and rendering.
    """
    
    def __init__(self):
        """
        Initialize the plane with default position, size, and animations.
        """
        self.width = 50
        self.height = 25
        self.images = self.create_plane_images()
        self.current_image = 0
        self.animation_counter = 0
        self.rect = self.images[0].get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.velocity = 0
        self.angle = 0
        self.max_angle = 30
        self.flame_animation = self.create_flame_animation()
        self.flame_counter = 0
        self.engine_on = False

    def create_plane_images(self):
        """
        Creates the animation frames for the plane.
        
        Returns:
            list: A list of plane surface images for animation
        """
        images = []
        for frame in range(3):
            img = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

            # Keha (hall)
            pygame.draw.ellipse(img, GREY,
                                (5, 5, self.width - 10, self.height - 10))

            # Tiivad (tumedam hall)
            pygame.draw.polygon(img, (50, 50, 50), [
                (self.width * 0.2, self.height * 0.4),
                (self.width * 0.1, self.height * 0.5),
                (self.width * 0.7, self.height * 0.5)
            ])

            # Kabiin (must)
            pygame.draw.ellipse(img, BLACK,
                                (self.width * 0.6, self.height * 0.2, 15, 15))

            # Stabilisaatorid (tagumised tiivad)
            pygame.draw.polygon(img, (60, 60, 60), [
                (self.width * 0.8, self.height * 0.7),
                (self.width * 0.9, self.height * 0.6),
                (self.width, self.height * 0.8)
            ])

            # Animaatioefekt - veidi muudetud tiiva asendit
            if frame == 1:
                pygame.draw.line(img, (40, 40, 40),
                                 (self.width * 0.2, self.height * 0.4),
                                 (self.width * 0.6, self.height * 0.4), 2)
            elif frame == 2:
                pygame.draw.line(img, (40, 40, 40),
                                 (self.width * 0.25, self.height * 0.35),
                                 (self.width * 0.65, self.height * 0.45), 2)

            images.append(img)
        return images

    def create_flame_animation(self):
        """
        Creates the animation frames for the plane's engine flame.
        
        Returns:
            list: A list of flame surface images for animation
        """
        frames = []
        colors = [
            (255, 100, 0, 200),
            (255, 150, 0, 180),
            (255, 200, 0, 160),
            (255, 255, 0, 140)
        ]

        for i in range(4):
            frame = pygame.Surface((20, 15), pygame.SRCALPHA)
            points = []
            for j in range(4):
                x = j * 5
                y = 7 + math.sin(j + i) * 5
                points.append((x, y))
            pygame.draw.polygon(frame, colors[i], points)
            frames.append(frame)

        return frames

    def flap(self):
        """
        Makes the plane jump upward.
        Activates the engine and resets velocity.
        """
        self.velocity = FLAP_STRENGTH
        self.engine_on = True
        self.flame_counter = 0

    def update(self):
        """
        Updates the plane's position, physics, and animation state.
        Should be called once per frame.
        """
        # Gravitatsioon
        self.velocity += GRAVITY
        self.rect.y += int(self.velocity)

        # Nurk vastavalt kiirusele
        self.angle = min(max(-self.velocity * 3, -self.max_angle),
                         self.max_angle)

        # Animatsioon
        self.animation_counter += 0.1
        if self.animation_counter >= len(self.images):
            self.animation_counter = 0
        self.current_image = int(self.animation_counter)

        # Leekude animatsioon
        if self.engine_on:
            self.flame_counter += 0.2
            if self.flame_counter >= len(self.flame_animation):
                self.flame_counter = 0
                self.engine_on = False

    def draw(self, surface):
        """
        Draws the plane and its flame animation on the given surface.
        
        Args:
            surface: The pygame surface to draw on
        """
        # Pööratud pildi loomine
        rotated_img = pygame.transform.rotate(self.images[self.current_image],
                                              self.angle)
        new_rect = rotated_img.get_rect(center=self.rect.center)
        surface.blit(rotated_img, new_rect)

        # Joonistame mootorileeku
        if self.engine_on and self.velocity < 0:
            flame_img = self.flame_animation[int(self.flame_counter)]

            # Arvutame leeku asendi lennuki suhtes
            flame_x = self.rect.x - math.cos(math.radians(self.angle)) * (
                        self.width // 2 + 10)
            flame_y = self.rect.y + math.sin(math.radians(self.angle)) * (
                        self.width // 2 + 10)

            # Pöörame leeku vastavalt lennuki suunale
            rotated_flame = pygame.transform.rotate(flame_img, self.angle)
            flame_rect = rotated_flame.get_rect(center=(flame_x, flame_y))
            surface.blit(rotated_flame, flame_rect)
