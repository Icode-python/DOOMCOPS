from settings import *
from sprite_objects import *
import pygame
import math

#sprites = Sprites()

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
        self.hit_rect = pygame.Rect(self.x, self.y, TILE * 10, TILE * 10)
        self.vx, self.vy = 0,0

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        #print(self.angle)
        if self.angle >= ANGLE_CLAMP or self.angle <= -ANGLE_CLAMP:
            self.angle = 0
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        collidewithwalls(self,'x')
        self.rect.y = self.y
        collidewithwalls(self,'y')
        self.hit_rect.move(self.rect.x, self.rect.y)
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
        if keys[pygame.K_LEFT]:
            self.angle -= SENSITIVITY
        if keys[pygame.K_RIGHT]:
            self.angle += SENSITIVITY
        if keys[pygame.K_a]:
            self.vx += player_speed * sin_a
            self.vy += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.vx = -player_speed * sin_a
            self.vy = player_speed * cos_a
        if keys[pygame.K_SPACE]:
            bullet(self.x, self.y, player_speed * cos_a, player_speed * sin_a)
            #print(self.vx, self.vy)
        if mousepos[0] < HALF_WIDTH:
            pygame.mouse.set_pos(HALF_WIDTH,HALF_HEIGHT)
            self.angle -= MOUSE_SENSITIVITY
        if mousepos[0] > HALF_WIDTH:
            pygame.mouse.set_pos(HALF_WIDTH,HALF_HEIGHT)
            self.angle += MOUSE_SENSITIVITY
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullet(self.x, self.y, player_speed * cos_a, player_speed * sin_a)

class bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy,width=10,height=10):
        #print('spawned')
        self.groups = all_sprites, bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 5
        self.vx, self.vy = vx, vy
    
    def update(self):
        #print('called')
        #print(self.vx, self.vy)
        self.x += self.vx * self.speed
        self.y += self.vy * self.speed
        self.rect.x = self.x
        if collidewithwalls(self,'x'):
            self.kill()
        self.rect.y = self.y
        if collidewithwalls(self,'y'):
            self.kill()

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

list_of_objects = []

class mob(pygame.sprite.Sprite):
    def __init__(self,x,y,width=64,height=64):
        self.groups = all_sprites, mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.follow_radius = pygame.Rect(x, y, TILE * 200, TILE * 200)
        self.rect.x = self.x
        self.rect.y = self.y
        self.vx, self.vy = 0, 0
        #for x in range(0,3):
        self.sprite = SpriteObject(pygame.image.load('img/demon.png'), True, (self.x // TILE, self.y // TILE), 1.6, 0.5, 2, 150)
        list_of_objects.append(self.sprite)
        #print(self.sprite.object)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        collidewithwalls(self,'x')
        self.rect.y = self.y
        collidewithwalls(self,'y')
        self.sprite.x, self.sprite.y = self.x, self.y
        #self.move()

    def move(self, targetx, targety, player):
        self.vx, self.vy = 0,0
        if self.follow_radius.colliderect(player.hit_rect):
            if self.x < targetx:
                self.vx += MOBSPEED
            if self.x > targetx:
                self.vx -= MOBSPEED
            if self.y < targety:
                self.vy += MOBSPEED
            if self.y > targety:
                self.vy -= MOBSPEED
    
    def collisionPlayer(self):
       #print('called')
        hits = pygame.sprite.spritecollide(self, players, False)
        if hits:
            self.kill()
            list_of_objects.pop(list_of_objects.index(self.sprite))
        hits = pygame.sprite.spritecollide(self, bullets, False)
        if hits:
            self.kill()
            list_of_objects.pop(list_of_objects.index(self.sprite))