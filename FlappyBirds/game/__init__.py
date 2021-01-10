import pygame
import sys
from game.constants import Constants
from game.floor import Floor
from game.plane import Plane
from game.pillars import Pillars

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.game_over = False
        self.game_over_text = pygame.image.load('assets/textGameOver.png').convert_alpha()

        self.bg_surface = pygame.image.load('assets/background.png').convert()

        self.all_sprites = pygame.sprite.Group()
        self.floor = Floor(self.all_sprites)
        self.player = Plane()
        self.pillars = Pillars(self.all_sprites)
        self.all_sprites.add(self.player)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.game_over:
                self.reset()
            else:
                self.player.apply_up()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def reset(self):
        self.player.reset()
        self.pillars.reset()
        self.game_over = False

    def draw(self):
        if self.game_over:
            self.screen.blit(self.game_over_text, (200, 200))
            pygame.display.flip()
        else:
            self.screen.blit(self.bg_surface, (0, 0))
            self.all_sprites.draw(self.screen)

    def update(self):
        if self.game_over:
            pass
        else:
            self.pillars.update()
            self.all_sprites.update()
            pygame.display.update()
            self.clock.tick(120)

            if self.floor.player_did_collide(self.player) or self.pillars.player_did_collide(self.player):
                self.game_over = True
