import pygame
from game.constants import Constants


class Floor:
    def __init__(self, sprite_group):
        self.ground1 = Ground()
        self.ground2 = Ground(808)

        self.floor_sprites = pygame.sprite.Group()
        self.floor_sprites.add(self.ground1, self.ground2)

        sprite_group.add(self.ground1, self.ground2)

    def player_did_collide(self, player):
        if pygame.sprite.spritecollide(player, self.floor_sprites, False, collided=pygame.sprite.collide_mask):
            return True
        return False


class Ground(pygame.sprite.Sprite):
    def __init__(self, offset=0):
        super().__init__()
        self.offset = offset
        self.x_pos = 404 + self.offset
        self.y_pos = Constants.screen_height - 35
        self.delta = 1
        self .image = pygame.image.load('assets/groundGrass.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    def update(self):
        self.x_pos -= self.delta
        if self.x_pos < -404 + self.offset:
            self.x_pos = 404 + self.offset

        self.rect.center = (self.x_pos, self.y_pos)
