import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    user_ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    
    aliens = Group()
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, user_ship, bullets)
        user_ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, user_ship, alien, bullets)
        
run_game()