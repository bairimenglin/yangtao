import pytest
from game_stats import GameStats
from settings import Settings

@pytest.fixture
def stats():
    ai_settings = Settings()
    return GameStats(ai_settings)

def test_initialization(stats):
    assert stats.ships_left == stats.ai_settings.ship_limit
    assert stats.score == 0
    assert stats.level == 1

def test_reset_stats(stats):
    stats.ships_left = 2
    stats.score = 100
    stats.level = 3

    stats.reset_stats()

    assert stats.ships_left == stats.ai_settings.ship_limit
    assert stats.score == 0
    assert stats.level == 1

def test_game_active(stats):
    assert not stats.game_active

def test_high_score(stats):
    assert stats.high_score == 0
