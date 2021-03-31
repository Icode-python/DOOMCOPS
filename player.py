from settings import *
import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = players
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x, self.y = x, y
        self.angle = player_angle
        self.width = 12
        self.height = 12
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0,0

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        collidewithwalls(self,'x')
        self.rect.y = self.y
        collidewithwalls(self,'y')
        #print(self.vx, self.vy)
        self.vx, self.vy = 0,0
        mousepos = pygame.mouse.get_pos()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.vx += player_speed * cos_a
            self.vy += player_speed * sin_a
        if keys[pygame.K_s]:
            self.vx += -player_speed * cos_a
            self.vy += -player_speed * sin_a
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            #self.vx += player_speed * sin_a
            #self.vy += -player_speed * cos_a
            self.angle -= SENSITIVITY
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            #self.vx = -player_speed * sin_a
            #self.vy = player_speed * cos_a
            self.angle += SENSITIVITY
        if mousepos[0] < HALF_WIDTH:
            pygame.mouse.set_pos(HALF_WIDTH,HALF_HEIGHT)
            self.angle -= SENSITIVITY
        if mousepos[0] > HALF_WIDTH:
            pygame.mouse.set_pos(HALF_WIDTH,HALF_HEIGHT)
            self.angle += SENSITIVITY

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width=TILE, height=TILE):
        self.groups = Walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class mob(pygame.sprite.Sprite):
    def __init__(self,x,y,width=12,height=12):
        self.groups = all_sprites, mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vx, self.vy = 0, 0
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        collidewithwalls(self,'x')
        self.rect.y = self.y
        collidewithwalls(self,'y')
        #self.move()

    def move(self, targetx, targety):
        self.vx, self.vy = 0,0
        if self.x < targetx:
            self.vx += MOBSPEED
        if self.x > targetx:
            self.vx -= MOBSPEED
        if self.y < targety:
            self.vy += MOBSPEED
        if self.y > targety:
            self.vy -= MOBSPEED
    
    def collisionPlayer(self):
        pygame.sprite.spritecollide(self, players, True)