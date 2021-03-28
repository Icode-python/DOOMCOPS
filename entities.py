import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, game):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 60
        self.height = 110
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y - self.height/2 + 10
        self.mass = 1
        self.speed = 5

    def update(self):
        self.draw()
        self.keys()
        if not self.collideWithWalls('floor'):
            self.rect.y += self.mass * self.game.gravity

    def draw(self):
        pass
        #self.game.draw(self.image, self.rect.centerx, self.rect.centery)
    
    def keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d or pygame.K_RIGHT]:
            self.move(self.speed,0)
    
    def move(self, dx=0, dy=0):
        if not self.collideWithWalls('side'):
            self.rect.x += dx
            self.rect.y += dy
    
    def collideWithWalls(self, facing):
        if pygame.sprite.spritecollideany(self, self.game.walls):
            for wall in self.game.walls:
                if facing == wall.facing:
                    print(facing, wall.facing)
                    #print("true")
                    return True
        else:
            return False
