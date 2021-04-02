import pygame
from settings import *
from player import Player
import math
from map import *
from sprite_objects import *
from ray_casting import *
from drawing import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
pygame.display.set_caption('DOOM RIP OFF XD')
clock = pygame.time.Clock()
#player = Player()
pygame.mouse.set_visible(False)

sprites = Sprites()
drawing = Drawing(sc, sc_map)
cursor = pygame.Surface((10,10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    player.movement()
    sc.fill(BLACK)
    #drawing.background()
    all_sprites.update()

    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.world(obj.object_locate(player, walls) for obj in list_of_objects)
    #drawing.world(walls + [mob.sprite.object_locate(player, walls) for mob in mobs])
    drawing.fps(clock)
    drawing.mini_map(player)

    for mob in mobs:
        mob.move(player.x, player.y, player)
        mob.collisionPlayer()
    #drawing.drawMob()
        #enemyRay_casting(sc, player.pos, player.angle)
    #ray_casting(sc, player.pos, player.angle)
    #for wall in Walls:
    #    sc.blit(wall.image, wall.rect)
    #for mob in mobs:
    #    sc.blit(mob.image, mob.rect)
    #for bullet in bullets:
    #    sc.blit(bullet.image, bullet.rect)
    #sc.blit(player.image, player.rect)
    sc.blit(cursor, (HALF_WIDTH, HALF_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())