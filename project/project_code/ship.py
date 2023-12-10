import pygame
from pygame.sprite import Sprite

import os
import sys


def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """ 初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(get_resource_path('images/g3.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕左部中央
        #self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 在飞船的属性center中存储小数值
        self.y = float(self.rect.y)

        """ 移动标志"""
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """ 根据移动标志调整飞船的位置
            更新飞船的center值，而不是rect"""
        if self.moving_top and self.rect.top >0:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom<self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor
        # 根据 self.center 更新 rect对象
        #self.rect.centerx = self.center
        self.rect.y = self.y
        
    def blit_me(self):
        """ 在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ 让飞船在屏幕上居中"""
        #self.center = self.screen_rect.centerx
        """ 让飞船在屏幕上左侧居中"""
        self.rect.midleft = self.screen_rect.midleft


