import pygame 
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self, screen):
        # инициализация пушки
        super(Gun, self).__init__()
        self.screen = screen 
        self.font_end = pygame.font.SysFont('Arial', 66, bold=True)
        self.image = pygame.image.load('images/wun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self):
        # рисование пушки 
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        # обновление позиции пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.7
        elif self.mleft and self.rect.left > 0:
            self.center -= 0.7

        self.rect.centerx = self.center

    def create_gun(self):
        # размещает пушку по центру внизу
        self.center = self.screen_rect.centerx
