import pygame
from settings import *
from player import Player
import math
from map import *
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DOOM RIP OFF XD')
clock = pygame.time.Clock()
#player = Player()
pygame.mouse.set_visible(False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    player.movement()
    sc.fill(BLACK)
    all_sprites.update()
    for mob in mobs:
        mob.move(player.x, player.y)
        mob.collisionPlayer()

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    ray_casting(sc, player.pos, player.angle)
    for wall in Walls:
        sc.blit(wall.image, wall.rect)
    for mob in mobs:
        sc.blit(mob.image, mob.rect)
    sc.blit(player.image, player.rect)

    #pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    #pygame.draw.line(sc, GREEN, player.pos, (player.rect.x + WIDTH * math.cos(player.angle),
    #                                          player.rect.y + WIDTH * math. sin(player.angle)), 2)
    #for x,y in world_map:
    #    pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())