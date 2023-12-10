import pygame
from bullet import Bullet
from settings import Settings
from ship import Ship

def test_bullet_initialization():
    ai_settings = Settings()
    screen = pygame.Surface((800, 600))
    ship = Ship(ai_settings, screen)
    
    # 创建一个子弹对象
    bullet = Bullet(ai_settings, screen, ship)

    # 验证子弹对象的属性是否正确设置
    #assert bullet.rect.x == 0
    #assert bullet.rect.y == 0
    #assert bullet.rect.centerx == ship.rect.centerx
    assert bullet.rect.midright == ship.rect.midright
    #assert bullet.x == 0.0
    assert bullet.color == ai_settings.bullet_color
    assert bullet.speed_factor == ai_settings.bullet_speed_factor

def test_bullet_update():
    ai_settings = Settings()
    screen = pygame.Surface((800, 600))
    ship = Ship(ai_settings, screen)
    
    # 创建一个子弹对象
    bullet = Bullet(ai_settings, screen, ship)

    # 更新子弹位置
    bullet.update()

    # 验证子弹位置是否正确更新
    #assert bullet.x == 0.0 + ai_settings.bullet_speed_factor
    assert bullet.rect.x == int(bullet.x)

def test_bullet_draw_bullet():
    ai_settings = Settings()
    screen = pygame.Surface((800, 600))
    ship = Ship(ai_settings, screen)
    
    # 创建一个子弹对象
    bullet = Bullet(ai_settings, screen, ship)

    # 绘制子弹
    bullet.draw_bullet()

    # 检查是否在屏幕上绘制了子弹


