import pygame
from pygame.sprite import Sprite
from random import randint

 
class Star(Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.image = pygame.image.load('images\sun233.png')
        # 在这里随机缩小星星大小
        random_size = randint(10, 30)
        self.image = pygame.transform.smoothscale(self.image,(random_size, random_size))
        self.rect = self.image.get_rect()
