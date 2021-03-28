import pygame
from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, facing, sprite='none'):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if sprite =='none':
            self.image = pygame.Surface((TILESIZE, TILESIZE))
        else:
            self.image = sprite
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.hit_rect = self.image.get_rect(center=(x * TILESIZE + TILESIZE/2, y * TILESIZE + TILESIZE/2))
        #self.hit = pygame.Surface((TILESIZE,TILESIZE))
        #self.hit.fill(BLACK)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.facing = facing