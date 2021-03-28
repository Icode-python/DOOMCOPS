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
        self.mass = 5
        self.speed = 5
        self.jumppower = 3
        self.jumpheight = PLAYERJUMPHEIGHT
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.standing = False

    def update(self):
        self.draw()
        self.keys()
        self.jump()
        if not self.collideWithFloor():
            self.rect.y += self.mass * self.game.gravity

    def draw(self):
        pass
        #self.game.draw(self.image, self.rect.centerx, self.rect.centery)
    
    def keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w or pygame.K_UP]:
            if self.up != True and self.collideWithFloor():
                self.up = True
                self.left = False
                self.right = False
        elif keys[pygame.K_d or pygame.K_RIGHT]:
            self.move(self.speed,0)
            self.right = True
            self.left = False
        elif keys[pygame.K_a or pygame.K_LEFT]:
            self.move(-self.speed,0)
            self.right = False
            self.left = True

    def jump(self):
        print(self.jumpheight)
        if self.up == True:
            if self.jumpheight >= 0:
                self.rect.y -= self.mass * 2
                self.jumpheight -= 1
            else:
                self.jumpheight = PLAYERJUMPHEIGHT
                self.up = False

    def move(self, dx=0, dy=0):
        if not self.collideWithWalls():
            self.rect.x += dx
            self.rect.y += dy
    
    def collideWithWalls(self):
        if pygame.sprite.spritecollideany(self, self.game.walls):
            if self.right is True:
                self.rect.x -= 10
            if self.left is True:
                self.rect.x += 10
            return True
        else:
            return False

    def collideWithFloor(self):
        if pygame.sprite.spritecollideany(self, self.game.floor):
            return True
        else:
            return False
