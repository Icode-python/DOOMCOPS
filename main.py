import pygame
from settings import *
from player import Player
import math
from map import *
from sprite_objects import *
from ray_casting import *
from drawing import *
import sys

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
pygame.display.set_caption('AMERICA RIP OFF XD')
clock = pygame.time.Clock()
#player = Player()
ls = levelSystem()
ls.generateLevel()
player = ls.player
pygame.mouse.set_visible(False)

sprites = Sprites()
drawing = Drawing(sc, sc_map)
cursor = pygame.Surface((10,10))
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_SPACE and paused == False:
                if len(bulletlist) < 2 and player.ammo > 0:
                    GUNSOUND.play()
                    bulletlist.append(bullet(player.x, player.y, player_speed * player.cos_a, player_speed * player.sin_a))
                    player.ammo -= 1
            if event.key == pygame.K_TAB:
                paused = not paused
        if event.type == pygame.MOUSEBUTTONDOWN and paused == False:
            if event.button == 1:
                if len(bulletlist) < 2 and player.ammo > 0:
                    GUNSOUND.play()
                    bulletlist.append(bullet(player.x, player.y, player_speed * player.cos_a, player_speed * player.sin_a))
                    player.ammo -= 1
    if paused == False:
        player.movement()
        sc.fill(BLACK)
        #drawing.background()
        for mob in mobs:
            mob.move(player.x, player.y, player)
            mob.collisionPlayer(player)
        all_sprites.update()

        drawing.background(player.angle)
        walls = ray_casting_walls(player, drawing.textures, ls.world_map, ls.width, ls.height)
        drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
        drawing.world(obj.object_locate(player, walls) for obj in list_of_objects)
        drawing.player(player)
        #drawing.world(walls + [mob.sprite.object_locate(player, walls) for mob in mobs])
        drawing.fps(clock)
        #drawing.mini_map(player)
        if len(mobs) == 0:
            #for sprites in all_sprites:
            #    sprites.kill()
            ls.levelNumber += 1
            if ls.levelNumber < len(ls.levels):
                list_of_objects.clear()
                sprites.list_of_objects.clear() 
                ls.generateLevel()
                player = ls.player
            else:
                pygame.quit()
                sys.exit()
        #drawing.drawMob()
            #enemyRay_casting(sc, player.pos, player.angle)
        #wwray_casting(sc, player.pos, player.angle)
        #for wall in Walls:
        #    sc.blit(wall.image, wall.rect)
        #for mob in mobs:
        #    sc.blit(mob.image, mob.rect)
        #for b in bullets:
        #    sc.blit(b.image, b.rect)
        #sc.blit(player.image, player.rect)
        sc.blit(cursor, (HALF_WIDTH, HALF_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())