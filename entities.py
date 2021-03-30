import pygame
from settings import *
from tilemap import collideWithWalls

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, game):
        self.game = game
        self.groups = game.all_sprites, game.players
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
        #print(self.vx)
        #print(self.down, self.up)
        self.draw()
        self.keys()
        self.jump()
            #self.rect.x, self.rect.y = self.x, self.y - self.height/2 + 10
        self.x += self.vx * self.game.dt
        self.y += self.vy  
        self.rect.x = self.x
        collideWithWalls(self, 'x')
        self.rect.y = self.y
        collideWithWalls(self, 'y')

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
        if not collideWithWalls(self, 'else'):
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
        if keys[pygame.K_w] or keys[pygame.K_UP]:
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
            #self.jumpheight = PLAYERJUMPHEIGHT
        elif keys[pygame.K_SPACE]:
            pass

    def jump(self):
        collideWithWalls(self)
        if self.up == True:
            if self.jumpheight >= 0:
                self.vy = -GRAVITY
                self.jumpheight -= 1
            else:
                self.jumpheight = PLAYERJUMPHEIGHT
                self.up = False


class mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        #self.kill_radius = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE * 20, TILESIZE * 20)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.vy, self.vx = 0,0
        self.moveDelay = 0
        self.chance = 1
        self.speed = 40
        self.dir = 1
    
    def update(self):
        #print(self.x)
        self.x += self.vx + self.dir * 5
        self.y += self.vy
        self.rect.x = self.x
        collideWithWalls(self, 'x')
        self.rect.y = self.y
        collideWithWalls(self, 'y')
        self.move(self.game.player.x, self.game.player.y)

    def move(self, x, y):
        self.vy = 0
        self.vy += GRAVITY
        #self.kill_radius.center = self.rect.center
        #if self.kill_radius.colliderect(self.game.player.rect):
        collideWithWalls(self, 'elsex')
            #self.dir = self.dir * -1
        #self.x += 10 * self.dir
        self.collisionplayer()

    def collisionplayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, velx, vely):
        self.groups = game.all_sprites, game.Bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE / 2, TILESIZE / 2))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.kill_timer = 0
    
    def update(self):
        self.x += self.velx
        self.collision()
    
    def collision(self):
        hits = pygame.sprite.spritecollide(self, self.game.walls, True)
        hits = pygame.sprite.spritecollide(self, self.game.mobs, True)