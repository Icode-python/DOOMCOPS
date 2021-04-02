from settings import *
from sprite_objects import *
import pygame
import math

pygame.init()
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
        self.health = 5
        self.reloadCount = 0
        self.gunAnimationCount = 0
        self.currentWeapon = 0
        self.weapons = []
        self.cos_a, self.sin_a = 0,0 
        self.ammo = AMMO
        for x in range(0,3):
            self.weapons.append(pygame.image.load('img/gun/{}.png'.format(x)))
            self.weapons[x] = pygame.transform.scale2x(self.weapons[x])

    @property
    def pos(self):
        return (self.x, self.y)
    
    def collision(self):
        if self.health <= 0:
            pygame.quit()
    
    def gunAnimation(self):
        self.currentWeapon = self.reloadCount
        self.gunAnimationCount += 1
        if self.gunAnimationCount == 5:
            self.reloadCount += 1
            self.gunAnimationCount = 0
        if self.reloadCount == 3:
            self.ammo = AMMO
            self.reloadCount = 0
            self.currentWeapon = 0


    def movement(self):
        if self.ammo <= 0:
            self.gunAnimation()
        self.collision()
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
        self.sin_a = math.sin(self.angle)
        self.cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.vx += player_speed * self.cos_a
            self.vy += player_speed * self.sin_a
        if keys[pygame.K_s]:
            self.vx += -player_speed * self.cos_a
            self.vy += -player_speed * self.sin_a
        if keys[pygame.K_LEFT]:
            self.angle -= SENSITIVITY
        if keys[pygame.K_RIGHT]:
            self.angle += SENSITIVITY
        if keys[pygame.K_a]:
            self.vx += player_speed * self.sin_a
            self.vy += -player_speed * self.cos_a
        if keys[pygame.K_d]:
            self.vx = -player_speed * self.sin_a
            self.vy = player_speed * self.cos_a
                #print(self.vx, self.vy)
        if mousepos[0] < HALF_WIDTH:
            pygame.mouse.set_pos(HALF_WIDTH,HALF_HEIGHT)
            self.angle -= MOUSE_SENSITIVITY
        if mousepos[0] > HALF_WIDTH:
            pygame.mouse.set_pos(HALF_WIDTH,HALF_HEIGHT)
            self.angle += MOUSE_SENSITIVITY

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
            bulletlist.pop(bulletlist.index(self))
            self.kill()
        self.rect.y = self.y
        collidewithwalls(self,'y')

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
        self.walk_cycle = 0
        self.sprite_change = 0
        self.standing = False
        #for x in range(0,3):
        self.sprite = SpriteObject(pygame.image.load('img/robber/0.png'), True, (self.x // TILE, self.y // TILE), 1.6, 0.5, 2, 150)
        list_of_objects.append(self.sprite)
        self.sprites = []
        for x in range(0,7):
            self.sprites.append(pygame.image.load('img/robber/{}.png'.format(x)))
        #print(self.sprite.object)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        collidewithwalls(self,'x')
        self.rect.y = self.y
        collidewithwalls(self,'y')
        self.sprite.x, self.sprite.y = self.rect.x + self.width, self.rect.y
        self.animation()
        #self.move()
    
    def animation(self):
        if not self.standing:
            if self.walk_cycle >= 6:
                self.walk_cycle = 0
            if self.sprite_change >= 10:
                self.walk_cycle += 1
                self.sprite_change = 0
            self.sprite_change += 1
            self.sprite.object = self.sprites[self.walk_cycle]
        else:
            self.walk_cycle = 0

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
        else:
            self.standing = False
    
    def collisionPlayer(self, player):
       #print('called')
        hits = pygame.sprite.spritecollide(self, players, False)
        if hits:
            self.kill()
            player.health -= 1
            list_of_objects.pop(list_of_objects.index(self.sprite))
        hits = pygame.sprite.spritecollide(self, bullets, False)
        if hits:
            self.kill()
            list_of_objects.pop(list_of_objects.index(self.sprite))