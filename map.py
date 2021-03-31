from settings import *
from player import *
from os import path

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

m = Map('mapexample.txt')

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

world_map = set()
mobset = set()
for j, row in enumerate(m.data):
    for i, char in enumerate(row):
        if char == '1':
            world_map.add((i * TILE, j * TILE))
            Wall(i * TILE,j * TILE)
        if char == 'P':
            player = Player(i * TILE, j * TILE)
        if char == 'E':
            mob(i * TILE, j * TILE)