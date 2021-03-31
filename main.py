import pygame
from settings import *
from player import Player
import math
from map import *
from ray_casting import ray_casting
from drawing import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
pygame.display.set_caption('DOOM RIP OFF XD')
clock = pygame.time.Clock()
#player = Player()
pygame.mouse.set_visible(False)

drawing = Drawing(sc, sc_map)

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
    for mob in mobs:
        mob.move(player.x, player.y)
        mob.collisionPlayer()
    ray_casting(sc, player.pos, player.angle)
    for wall in Walls:
        sc.blit(wall.image, wall.rect)
    for mob in mobs:
        sc.blit(mob.image, mob.rect)
    sc.blit(player.image, player.rect)

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())