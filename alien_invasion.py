import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stat import GameStats
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import game_funtions as gf


def run_game():
# Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)
    # Group for bullet
    bullets = Group()
    # Group for alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # alien = Alien(ai_settings, screen)

    while True:
    # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)




run_game()

