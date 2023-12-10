from settings import Settings

def test_initialize_dynamic_settings():
    """ 测试 initialize_dynamic_settings 方法 """
    settings = Settings()
    settings.initialize_dynamic_settings()
    assert settings.ship_speed_factor == 1.5
    assert settings.bullet_speed_factor == 3
    assert settings.alien_speed_factor == 1
    assert settings.fleet_direction == 1
    assert settings.alien_points == 12  # 初始值为10 * 1.2


def test_increase_speed():
    """ 测试 increase_speed 方法 """
    settings = Settings()
    settings.initialize_dynamic_settings()
    settings.increase_speed()
    assert settings.ship_speed_factor == 1.5 * 1.2
    assert settings.bullet_speed_factor == 3 * 1.2
    assert settings.alien_speed_factor == 1 * 1.2
    assert settings.alien_points == 14  # 初始值为12 * 1.2
