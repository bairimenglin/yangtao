import pytest  
import pygame  
from button import Button  
from settings import Settings  
  
def test_button_preparation():  
    pygame.init()   
    ai_settings = Settings()  # 创建必要的Settings对象  
    screen = pygame.display.set_mode((1200, 800))  # 创建屏幕对象  
    msg = "Play"  
    button = Button(ai_settings, screen, msg)  
    assert isinstance(button, Button)  # 断言对象是Button类的实例  
  
    assert button.width == 200  # 断言按钮宽度为200  
    assert button.height == 50  # 断言按钮高度为50  
    assert button.button_color == (33, 33, 33)  # 断言按钮颜色为(33, 33, 33)  
    assert button.text_color == (255, 255, 255)  # 断言文字颜色为(255, 255, 255)  

  
def test_draw_button():  
    pygame.init()   
    ai_settings = Settings()  # 创建必要的Settings对象  
    screen = pygame.display.set_mode((1200, 800))  # 创建屏幕对象  
    msg = "Play"  
    button = Button(ai_settings, screen, msg)  
    button.draw_button()  
    assert button.screen.get_rect().contains(button.rect)  # 断言屏幕矩形包含按钮矩形  
    assert button.screen.get_rect().contains(button.msg_image_rect)  # 断言屏幕矩形包含文本矩形