"""
Flappy Plane - A simple 2D game where a plane navigates through buildings.
"""
import pygame
import sys
from constants import *
from plane import Plane
from skyscraper import Skyscraper
from cloud import Cloud
from ground import Ground

def draw_score(surface, score, high_score):
    """
    Draws the current score and high score on the game surface.
    
    Args:
        surface: The pygame surface to draw on
        score: Current game score
        high_score: Highest score achieved
    """
    score_text = font.render(f"Score: {score}", True, BLACK)
    high_score_text = font.render(f"High: {high_score}", True, BLACK)
    surface.blit(score_text, (10, 10))
    surface.blit(high_score_text, (10, 50))

def show_game_over(surface, score, high_score):
    """
    Displays the game over screen with final score and restart instructions.
    
    Args:
        surface: The pygame surface to draw on
        score: Final score of the current game
        high_score: Highest score achieved
    """
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    surface.blit(overlay, (0, 0))

    game_over = font.render("GAME OVER", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_text = font.render(f"High Score: {high_score}", True, WHITE)
    restart = font.render("Press SPACE to restart", True, WHITE)

    surface.blit(game_over,
                 (SCREEN_WIDTH // 2 - game_over.get_width() // 2, 200))
    surface.blit(score_text,
                 (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 250))
    surface.blit(high_text,
                 (SCREEN_WIDTH // 2 - high_text.get_width() // 2, 300))
    surface.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, 350))

    pygame.display.update()

def main():
    """
    Main game loop and initialization.
    Handles game state, event processing, and rendering.
    """
    plane = Plane()
    skyscrapers = []
    clouds = [Cloud() for _ in range(5)]
    ground = Ground()
    last_pipe = pygame.time.get_ticks()
    score = 0
    high_score = 0
    game_active = False
    game_started = False
    pipe_speed = 2

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_started:
                        game_started = True
                        game_active = True
                    elif not game_active:
                        # Kui mäng lõppeb, alustame uut mängu
                        plane = Plane()
                        skyscrapers = []
                        clouds = [Cloud() for _ in range(5)]
                        score = 0
                        pipe_speed = 2
                        game_active = True
                    else:
                        # Kui mäng on aktiivne, siis lennuk hüppab ülespoole
                        plane.flap()

        screen.fill(SKY_BLUE)

        # Pilved
        for cloud in clouds[:]:
            if cloud.update():
                clouds.remove(cloud)
                clouds.append(Cloud())
            cloud.draw(screen)

        if game_active:
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > PIPE_FREQUENCY:
                skyscrapers.append(Skyscraper(SCREEN_WIDTH))
                last_pipe = time_now
                pipe_speed = min(pipe_speed + 0.05, 5)  # Kiirus suureneb kuni maksimumini

            plane.update()

            for s in skyscrapers[:]:
                s.update(pipe_speed)

                if not s.passed and s.top.right < plane.rect.left:
                    s.passed = True
                    score += 1
                    high_score = max(high_score, score)

                if s.top.right < 0:
                    skyscrapers.remove(s)

            for s in skyscrapers:
                if s.collide(plane):
                    game_active = False

            if plane.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
                plane.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
                game_active = False

            if plane.rect.top <= 0:
                plane.rect.top = 0
                plane.velocity = 0

        for s in skyscrapers:
            s.draw(screen)

        plane.draw(screen)
        ground.update()
        ground.draw(screen)
        draw_score(screen, score, high_score)

        if not game_started:
            start_text = font.render("Press SPACE to start", True, WHITE)
            screen.blit(start_text,
                        (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 300))

        if game_started and not game_active:
            show_game_over(screen, score, high_score)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    # Initsialiseerimine
    pygame.init()
    pygame.mixer.init()
    
    # Ekraani seadistamine
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Plane")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 30)
    
    main()
