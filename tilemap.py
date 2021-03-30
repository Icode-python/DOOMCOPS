import pygame
from settings import *

def collideWithWalls(self, dir=None):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.grounded = True
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
        
        if dir == 'else':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                return True
        
        if dir == 'elsex':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vx = self.vx * -1
                return True

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
    def __init__(self, game, x, y, groups, sprite='none'):
        if groups == 'walls':
            self.groups = game.all_sprites,game.walls
        if groups == 'floor':
            self.groups = game.all_sprites,game.floor
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

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        #limit scrolling to map size
        #x = min(0, x)  # left
        #y = min(0, y)  # top
        #x = max(-(self.width - WIDTH), x)  # right
        #y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)