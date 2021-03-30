import pygame
import numpy as np
import sys
from os import path
from settings import *
from entities import *
from tilemap import *
import threading

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.enemies = []
        self.bullets = []
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, "mapexample.txt"))

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row, 'walls')
                if tile == "2":
                    Wall(self, col, row, 'floor')
                if tile == "P":
                    self.player = Player(col, row, self)
                if tile == "E":
                    mob(self,col,row)
        
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()
            self.events()
    
    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self, sprite=None, x=None, y=None):
        self.screen.fill(BACKGROUND_COLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #self.screen.blit(self.player.hit, self.player.hit_rect)
        #for wall in self.walls:
        #    self.screen.blit(wall.hit, wall.hit_rect)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

g = Game()
while True:
    g.new()
    g.run()