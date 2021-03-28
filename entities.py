import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, game):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.image = pygame.Surface((60,110))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.draw()

    def draw(self):
        pass
        #self.game.draw(self.image, self.rect.centerx, self.rect.centery)
