import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """Ship initialization"""

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/shipA.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #self.rect = pygame.transform.scale(self.rect, (20, 20))

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.screen_rect.bottom)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #self.ship_speed_factor = ai_settings.ship_factor

    def blitme(self):
        "Draw ship in current position"

        self.screen.blit(self.image, self.rect)

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_factor

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom


    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom