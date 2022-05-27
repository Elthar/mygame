import pygame
import random
import sys
import time
import pygame_menu
import os

MAX_X = 1366
MAX_Y = 768
MAX_SNOW = 100
SNOW_SIZE = 64
RES = 800
SIZE = 50

class Snow():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 2)
        self.img_num = random.randint(1, 4)
        self.image_filename = "images/ufo1.png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0 - SNOW_SIZE)

        i = random.randint(1, 3)
        if i == 1:   # дергается вправо
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        if i == 2:  # дергаетсч влево
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))


def initilize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx = random.randint(0, MAX_X)
        yy = random.randint(0, MAX_Y)
        snowfall.append(Snow(xx, yy))
   
def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                    # вправо
            if event.key == pygame.K_e:
                os.system('python our_game.py')

        
            

pygame.init()

screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0 ,0 ,0)
snowfall = []
rgb = 102, 193, 242
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
initilize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    render_end = font_end.render('GAME OVER:(', 1, pygame.Color('purple'))
    surface.blit(render_end, (RES // 2 - 230, RES // 3))
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.0020)
    pygame.display.flip()

    def update_animation(self, seconds):
        self.timer += seconds
        if self.timer >= self.time_interval:
            self.index = (self.index + 1) % len(self.images)
            self.timer = 0
    


