import pygame, sys
from bullet import Bullet
from alien import Alien
import time 
import os
import pygame_menu

RES = 800
SIZE = 50
FPS = 60

pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
shoot_song = pygame.mixer.Sound('audio/pew.wav')

def events(screen, gun, bullets):
    # обработка событий
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # вправо
                    if event.key == pygame.K_d:
                        gun.mright = True
                    elif event.key == pygame.K_a:
                        gun.mleft = True
                    elif event.key == pygame.K_SPACE:
                        new_bullet = Bullet(screen, gun)
                        bullets.add(new_bullet)
                        shoot_song.play()
                        
                elif event.type == pygame.KEYUP:
                    # вправо
                    if event.key == pygame.K_d:
                        gun.mright = False
                    if event.key == pygame.K_a:
                        gun.mleft = False

def update(bg_color, screen, stats, sc, gun, aliens, bullets):
    # обновление экрана
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, aliens, bullets):
    # обновлять позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions :
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    
    if len(aliens) == 0:
        bullets.empty()
        create_army01(screen, aliens)

def gun_kill(stats, screen, sc, gun, aliens, bullets):
    # столкновение пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(0.5)
    else:
        while True:
            os.system('python animation.py') 
            sys.exit()

def update_aliens(stats, screen, sc, gun, aliens, bullets):
    # обновляет позицию пришельцов
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, sc, gun, aliens, bullets)
    aliens_check(stats, screen, sc, gun, aliens, bullets)

def aliens_check(stats, screen, sc, gun, aliens, bullets):
    # проверяем добралась ли армия до края экрана
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, aliens, bullets)
            break

def create_army(screen, aliens):
    #создание армии пришельцев
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((700 - 450 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)

def create_army01(screen, aliens):
    #создание армии 5
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((700 - 380 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)

def check_high_score(stats, sc):
    # проверка новых рекордов
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))


