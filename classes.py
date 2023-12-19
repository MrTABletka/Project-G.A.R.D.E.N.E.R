import pygame
import random

WIDTH = 1000
HEIGHT = 800
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = speedy
        self.speedx = speedx
        self.damage = damage

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

    def get_damage(self):
        return self.damage

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hit_points = 4
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, HEIGHT)

    def update(self):
        if self.hit_points <= 0:
            self.kill()

class Gun():
    def __init__(self, damage):
        self.damage = damage
        self.current_ammo = 7
        self.ammo_max = 7
        self.total_ammo = 28
        self.fire_rate = 20
        self.reload = 0

    def shoot(self, x, y, sp_x, sp_y):
        if self.current_ammo != 0:
            self.current_ammo -= 1
            bullet = Bullet(x, y, sp_x, sp_y, self.damage)
            all_sprites.add(bullet)
            bullets.add(bullet)
            self.reload = self.fire_rate
        else:
            self.reload_ammo()
    def reload_ammo(self):
        self.reload = 120
        self.current_ammo = self.ammo_max
        self.total_ammo -= self.ammo_max

class Shotgun(Gun):
    def shoot(self, x, y, sp_x, sp_y):
        if self.current_ammo != 0:
            self.current_ammo -= 1
            bullet1 = Bullet(x, y, sp_x, sp_y, self.damage)
            all_sprites.add(bullet1)
            sp_x_2 = sp_x
            sp_y_2 = sp_y
            sp_x_3 = sp_x
            sp_y_3 = sp_y
            if sp_x > 0:
                if sp_y > 0:
                    sp_y_2 -= 3
                    sp_x_3 -= 3
                elif sp_y < 0:
                    sp_x_2 -= 3
                    sp_y_3 += 3
                else:
                    sp_y_2 -= 3
                    sp_y_3 += 3
            elif sp_x < 0:
                if sp_y > 0:
                    sp_x_2 += 3
                    sp_y_3 -= 3
                elif sp_y < 0:
                    sp_x_2 += 3
                    sp_y_3 += 3
                else:
                    sp_y_2 += 3
                    sp_y_3 -= 3
            else:
                sp_x_2 -= 3
                sp_x_3 += 3
            bullet2 = Bullet(x, y, sp_x_2, sp_y_2, self.damage)
            all_sprites.add(bullet2)
            bullet3 = Bullet(x, y, sp_x_3, sp_y_3, self.damage)
            all_sprites.add(bullet3)
            bullets.add(bullet3, bullet2, bullet1)
            self.reload = self.fire_rate
        else:
            self.reload_ammo()


class Assault_rifle(Gun):
    def __init__(self, damage):
        self.damage = damage
        self.ammo_max = 30
        self.current_ammo = 30
        self.total_ammo = 120
        self.fire_rate = 6
        self.reload = 0

all_sprites = pygame.sprite.Group()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()