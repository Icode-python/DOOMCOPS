from settings import *
from player import *
#from mapmakingscript import mapGeneration
from os import path
import random
#from main import sprites

filename = 'e'; rows = random.randint(0,50); columns = random.randint(0,50)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILE
        self.height = self.tileheight * TILE

#map = mapGeneration(rows, columns, filename)
#map.generate()
m = Map('e')

#text_map = [
#    'WWWWWWWWWWWW',
#    'W......W...W',
#    'W..WWW...W.W',
#    'W....W..WW.W',
#    'W..W.P..W..W',
#    'W..W...WWW.W',
#    'W....W.....W',
#    'WWWWWWWWWWWW'
#]

WORLD_WIDTH = 20 * TILE
WORLD_HEIGHT = 20 * TILE

world_map = {}
mini_map = set()
mobset = set()
for j, row in enumerate(m.data):
    for i, char in enumerate(row):
        if char != '_' and char != 'E' and char != 'P':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
                Wall(i * TILE,j * TILE)
            if char == '2':
                world_map[(i * TILE, j * TILE)] = '2'
                Wall(i * TILE,j * TILE)
        if char == 'P':
            player = Player(i * TILE, j * TILE)
        if char == 'E':
            mob(i * TILE, j * TILE)
            mobset.add((i * TILE, j * TILE))