import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, game):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE * 2
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y - self.height/2 + 10
        self.mass = 5
        self.speed = 5
        self.jumppower = 3
        self.jumpheight = PLAYERJUMPHEIGHT
        self.vx, self.vy = 0, 0
        self.up = False
        self.left = False
        self.right = False
        self.grounded = False

    def update(self):
        self.draw()
        self.keys()
        self.jump()
        self.x += self.vx * self.game.dt
        self.y += self.vy  
        self.rect.x = self.x
        self.collideWithWalls('x')
        self.rect.y = self.y
        self.collideWithWalls('y')

    def draw(self):
        pass
        #self.game.draw(self.image, self.rect.centerx, self.rect.centery)
    
    def keys(self):
        self.vx, self.vy = 0, 0
        self.vy += GRAVITY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w or pygame.K_UP] and self.grounded is True and self.up is False:
            #self.jump()
            self.grounded = False
            self.up = True
            self.left = False
            self.right = False
        elif keys[pygame.K_d or pygame.K_RIGHT]:
            self.vx = PLAYER_SPEED
            self.right = True
            self.left = False
        elif keys[pygame.K_a or pygame.K_LEFT]:
            self.vx = -PLAYER_SPEED
            self.right = False
            self.left = True

    def jump(self):
        if self.up == True:
            if self.jumpheight >= 0:
                self.vy = -GRAVITY
                self.jumpheight -= 1
            else:
                self.jumpheight = PLAYERJUMPHEIGHT
                self.up = False
    
    def collideWithWalls(self, dir):
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
                self.grounded = True
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
