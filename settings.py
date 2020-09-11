class Settings():
    """Class for storing all game settings"""

    def __init__(self):
        """Init game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.ship_limit = 3
        self.ship_factor = 1.5
        self.v_ship_factor = 1.5
        self.h_ship_factor = 1.5

        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 8

        self.alien_speed_factor = 0.5
        self.alien_points = 50
        self.fleet_drop_speed = 5
        self.fleet_direction = 1  # 1 - to right, -1 - to left
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)


