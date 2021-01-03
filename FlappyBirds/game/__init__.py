import pygame
import sys
from game.constants import constants


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_surface = pygame.image.load('assets/background.png').convert()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.k_SPACE]:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.blit(self.bg_surface, (0, 0))

    def update(self):
        pygame.display.update()
        self.clock.tick(120)
