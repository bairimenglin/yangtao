import pygame
import os
from ship import Ship


def get_test_ship(ai_settings, screen):
    """ 辅助函数：创建一个测试用的Ship实例 """
    test_ship = Ship(ai_settings, screen)
    test_ship.rect.centery = screen.get_rect().centery  # 将飞船放在屏幕中央
    return test_ship


def test_ship_init():
    """ 测试 Ship 类的 __init__ 方法 """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    ai_settings = object()
    test_ship = Ship(ai_settings, screen)
    
    assert test_ship.screen == screen
    assert test_ship.ai_settings == ai_settings
    
    image_path = os.path.join(os.path.abspath("."), 'images/g3.png')
    assert test_ship.image.get_rect().size == pygame.image.load(image_path).get_rect().size
    #assert test_ship.rect.center == (0, screen.get_rect().centery)
    #assert test_ship.y == 0
    assert test_ship.moving_top == False
    assert test_ship.moving_bottom == False
    
    

    
def test_ship_center_ship():
    """ 测试 Ship 类的 center_ship 方法 """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    ai_settings = object()
    test_ship = get_test_ship(ai_settings, screen)
    
    test_ship.center_ship()
    assert test_ship.rect.midleft == screen.get_rect().midleft




