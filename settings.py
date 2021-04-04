import math, pygame
pygame.mixer.init()

# game settings
WIDTH = 1200
HEIGHT = 700
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
SENSITIVITY = 0.3
MOUSE_SENSITIVITY = SENSITIVITY * 0.3
MOBSPEED = 1

# texture settings (1200, 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# sprite settings
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# player settings
AMMO = 1
ANGLE_CLAMP = 6
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 10
jumpheight = 10

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0,186,255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
BROWN = (74,37,0)

#sounds
GUNSOUND = pygame.mixer.Sound('sounds/gun_sound.wav')
MAINTHEME = pygame.mixer.Sound('sounds/gameMusic.wav')

bulletlist = []
Walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()

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
            return True
    elif dir == 'y':
        hits = pygame.sprite.spritecollide(self, Walls, False)
        if hits:
            if self.vy > 0:
                self.y = hits[0].rect.top - self.rect.height
            if self.vy < 0:
                self.y = hits[0].rect.bottom
            self.vy = 0
            self.rect.y = self.y
            return True
    elif dir == 'else':
        hits = pygame.sprite.spritecollide(self, Walls, False)
        if hits:
            return True
        else:
            return False