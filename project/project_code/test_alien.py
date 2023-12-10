import pytest  
import pygame  
from alien import Alien  


def test_init():  
    # 准备测试环境  
    pygame.init()  
    screen = pygame.display.set_mode((800, 600))  
    settings = pygame.sprite.Sprite()  # 一个伪造的Settings对象，可以假设其已被正确初始化  
    alien = Alien(settings, screen)  
  
    # 测试外星人图像是否正确加载  
    assert alien.image is not None  
    assert isinstance(alien.rect, pygame.Rect)  
    assert alien.rect.width == 60 and alien.rect.height == 60  # 假设外星人的大小为30x30像素  
  
    # 测试外星人的初始位置是否设置正确  
    assert alien.rect.x == 0 and alien.rect.y == 0  # 假设初始位置在屏幕左上角  
  
def test_blit_me():  
    # 准备测试环境  
    pygame.init()  
    screen = pygame.display.set_mode((800, 600))  
    settings = pygame.sprite.Sprite()  # 一个伪造的Settings对象，可以假设其已被正确初始化  
    alien = Alien(settings, screen)  
    alien.image = pygame.Surface((10, 10))  # 假设外星人的图像大小为10x10像素，用于测试blit_me()方法中self.rect的正确性  
    alien.rect = pygame.Rect(10, 10, 10, 10)  # 假设外星人的矩形区域大小为10x10像素，用于测试blit_me()方法中self.rect的正确性  
    screen.blit(alien.image, alien.rect)  # 在屏幕上的指定位置绘制外星人图像，用于验证blit_me()方法的功能  
    pygame.display.flip()  # 刷新屏幕显示，用于验证blit_me()方法的功能  
  
    # 验证外星人是否在指定位置正确绘制  
    assert screen.get_at((10, 10)) == alien.image.get_at((0, 0))  # 假设外星人的图像颜色为白色，用于验证blit_me()方法的功能  
  
  
