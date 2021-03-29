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
        self.crouchsize = self.height/2
        self.vx, self.vy = 0, 0
        self.up = False
        self.left = False
        self.right = False
        self.grounded = True
        self.down = False

    def update(self):
        #print(self.down, self.up)
        self.draw()
        self.keys()
        self.jump()
            #self.rect.x, self.rect.y = self.x, self.y - self.height/2 + 10
        self.x += self.vx * self.game.dt
        self.y += self.vy  
        self.rect.x = self.x
        self.collideWithWalls('x')
        self.rect.y = self.y
        self.collideWithWalls('y')

    def draw(self):
        pass
        #self.game.draw(self.image, self.rect.centerx, self.rect.centery)
    
    def crouching(self, yn):
        if yn == True:
            self.image = pygame.Surface((self.width, self.crouchsize))
            self.image.fill(YELLOW)
            #self.y += self.crouchsize 
            #self.rect.x, self.rect.y = self.x, self.y - self.height/2 + 10
            self.rect = self.image.get_rect()
        if yn == False:
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.y -= self.crouchsize
            #self.rect.x, self.rect.y = self.x, self.y - self.height/2 + 10
            
    def keys(self):
        self.vx, self.vy = 0, 0
        self.vy += GRAVITY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.crouching(False)
            self.down = False
            if self.grounded is True and self.up is False:
                #self.jump()
                self.grounded = False
                self.up = True
                self.left = False
                self.right = False
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vx = PLAYER_SPEED
            self.right = True
            self.left = False
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vx = -PLAYER_SPEED
            self.right = False
            self.left = True
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.crouching(True)
            self.down = True
            self.up = False
            self.jumpheight = PLAYERJUMPHEIGHT

    def jump(self):
        self.collideWithWalls()
        if self.up == True:
            if self.jumpheight >= 0:
                self.vy = -GRAVITY
                self.jumpheight -= 1
            else:
                self.jumpheight = PLAYERJUMPHEIGHT
                self.up = False
    
    def collideWithWalls(self, dir=None):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                print('collision')
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
