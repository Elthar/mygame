import pygame, control
from gun import Gun
from pygame.sprite import Group
from alien import Alien
from stats import Stats
from scores import Scores
import pygame_menu
import time

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("space defender")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    control.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)
    HELP =  'Press A to move left ' \
            '\nPress D to move right' \
            '\nPress SPACE to shot enemies ' 

    def start_the_game():

        while True:
            control.events(screen, gun, bullets)
            if stats.run_game:
                gun.update_gun()
                control.update(bg_color, screen, stats, sc, gun, aliens, bullets)
                control.update_bullets(screen, stats, sc, aliens, bullets)
                control.update_aliens(stats, screen, sc, gun, aliens, bullets)

    menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Play', start_the_game)
    menu.add.label(HELP, max_char=-1, font_size=20)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


run()



