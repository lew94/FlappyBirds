import pygame
import sys
from game.constants import Constants
from game.floor import Floor
from game.plane import Plane

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_surface = pygame.image.load('assets/background.png').convert()

        self.all_sprites = pygame.sprite.Group()
        self.floor = Floor(self.all_sprites)
        self.player = Plane()
        self.all_sprites.add(self.player)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.apply_up()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.blit(self.bg_surface, (0, 0))
        self.all_sprites.draw(self.screen)

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)
