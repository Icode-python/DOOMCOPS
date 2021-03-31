import math, pygame

# game settings
WIDTH = 1200
HEIGHT = 700
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
SENSITIVITY = 0.1
MOBSPEED = 1

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 5
jumpheight = 10

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)

Walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
players = pygame.sprite.Group()

def collidewithwalls(self, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(self, Walls, False)
        if hits:
            if self.vx > 0:
                self.x = hits[0].rect.left - self.rect.width
            if self.vx < 0:
                self.x = hits[0].rect.right
            self.vx = 0
            self.rect.x = self.x
    elif dir == 'y':
        hits = pygame.sprite.spritecollide(self, Walls, False)
        if hits:
            if self.vy > 0:
                self.y = hits[0].rect.top - self.rect.height
            if self.vy < 0:
                self.y = hits[0].rect.bottom
            self.vy = 0
            self.rect.y = self.y