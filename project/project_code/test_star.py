import pygame
from pygame.sprite import Sprite
from random import randint
from star import Star


def test_star_init():
    """ 测试 Star 类的 __init__ 方法 """
    pygame.init()
    test_star = Star()
    
    #assert test_star.image.get_rect().size == pygame.image.load('images\sun233.png').get_rect().size
    #assert test_star.rect.center == (0, 0)  # 由于没有指定位置，所以默认为(0, 0)
    
    
def test_star_random_scale():
    """ 测试随机缩放星星大小 """
    pygame.init()
    test_star = Star()
    
    assert 10 <= test_star.image.get_width() <= 30
    assert 10 <= test_star.image.get_height() <= 30
    
    
def test_star_update():
    """ 测试 Star 类的 update 方法 """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    test_star = Star()
    
    test_star.rect.x = 100
    test_star.rect.y = 200
    test_star.update()
    #assert test_star.rect.x == 99
    assert test_star.rect.y == 200
    
    test_star.rect.x = 0
    test_star.rect.y = -1
    test_star.update()
    assert test_star.rect.x == 0
    #assert test_star.rect.y == 600
    
    

