import pygame
import numpy as np
from settings import *
from entities import *
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
        pass

    def new(self):
        self.all_sprites = pygame.sprite.Group()