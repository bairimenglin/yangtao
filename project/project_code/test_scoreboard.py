import pygame
import pytest

from scoreboard import Scoreboard
from settings import Settings
from game_stats import GameStats


@pytest.fixture
def scoreboard():
    """ 创建一个新的 Scoreboard 实例 """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    stats = GameStats(ai_settings)
    return Scoreboard(ai_settings, screen, stats)


def test_prep_score(scoreboard):
    """ 测试 prep_score 方法 """
    scoreboard.prep_score()
    assert isinstance(scoreboard.score_iamge, pygame.Surface)
    #assert scoreboard.score_iamge.get_rect().top == 12


def test_prep_high_score(scoreboard):
    """ 测试 prep_high_score 方法 """
    scoreboard.prep_high_score()
    assert isinstance(scoreboard.high_score_iamge, pygame.Surface)
    #assert scoreboard.high_score_iamge.get_rect().centerx == scoreboard.screen_rect.centerx


def test_prep_level(scoreboard):
    """ 测试 prep_level 方法 """
    scoreboard.prep_level()
    assert isinstance(scoreboard.level_image, pygame.Surface)


def test_prep_ships(scoreboard):
    """ 测试 prep_ships 方法 """
    scoreboard.prep_ships()
    assert len(scoreboard.ships.sprites()) == scoreboard.stats.ships_left


def test_show_score(scoreboard):
    """ 测试 show_score 方法 """
    scoreboard.show_score()
    assert isinstance(scoreboard.score_iamge, pygame.Surface)
    assert isinstance(scoreboard.high_score_iamge, pygame.Surface)
    assert isinstance(scoreboard.level_image, pygame.Surface)
    assert isinstance(scoreboard.ships, pygame.sprite.Group)
    #assert scoreboard.score_iamge.get_rect().top == 12
    #assert scoreboard.high_score_iamge.get_rect().centerx == scoreboard.screen_rect.centerx
    #assert scoreboard.level_image.get_rect().top == scoreboard.score_rect.bottom + 10
