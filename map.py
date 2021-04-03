from settings import *
from player import *
#from mapmakingscript import mapGeneration
from os import path
import random
#from main import sprites

#filename = 'e'; rows = random.randint(0,50); columns = random.randint(0,50)
#WORLD_WIDTH = 20 * TILE
#WORLD_HEIGHT = 20 * TILE

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        #print(self.tilewidth, self.tileheight)
        self.width = self.tilewidth * TILE
        self.height = self.tileheight * TILE

#map = mapGeneration(rows, columns, filename)
#map.generate()
class levelSystem:
    def __init__(self):
        self.levelNumber = 0
        self.levels = []
        for x in range(0,20):
            self.levels.append('levels/{}'.format(x))
        self.player = 1
        self.world_map = {}
        self.mini_map = set()
        self.mobset = set()
        self.width = 0
        self.height = 0

    def generateLevel(self):
        self.map = Map(self.levels[self.levelNumber])
        self.width, self.height = self.map.width, self.map.height
        self.world_map.clear()
        self.mini_map.clear()
        self.mobset.clear()
        bulletlist.clear()
        mobs.empty()
        Walls.empty()
        all_sprites.empty()
        players.empty()
        for j, row in enumerate(self.map.data):
            for i, char in enumerate(row):
                if char != '.' and char != 'E' and char != 'P':
                    self.mini_map.add((i * MAP_TILE, j * MAP_TILE))
                    Wall(i * TILE,j * TILE)
                    if char == '1':
                        self.world_map[(i * TILE, j * TILE)] = '1'
                        Wall(i * TILE,j * TILE)
                    if char == '2':
                        self.world_map[(i * TILE, j * TILE)] = '2'
                        Wall(i * TILE,j * TILE)
                if char == 'P':
                    self.player = Player(i * TILE, j * TILE)
                if char == 'E':
                    mob(i * TILE, j * TILE)
                    self.mobset.add((i * TILE, j * TILE))

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