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

    def update(self):
        self.draw()
        self.keys()
        if not self.collideWithWalls():
            self.rect.y += self.mass * self.game.gravity

    def draw(self):
        pass
        #self.game.draw(self.image, self.rect.centerx, self.rect.centery)
    
    def keys(self):
        keys = pygame.key.get_pressed()
        if not self.collideWithWalls():
            if keys[pygame.K_d or pygame.K_RIGHT]:
                self.rect.x += 5
    
    def collideWithWalls(self):
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.rect.centery -= self.width/2
            print("collision")
            return True
        else:
            return False
