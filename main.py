import pygame
import random
import sys
from classes import (Enemy, Bullet, Gun, all_sprites, bullets, enemys, Shotgun, Assault_rifle, score, Box, Item, boxes,
                     Medkit, Ammo_box, Text, Signal_fire, fires)

WIDTH = 1920
HEIGHT = 1080
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (115, 135, 115)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gardener")
clock = pygame.time.Clock()


def show_stats(player, screen1):
    font1 = pygame.font.Font(None, 120)
    font2 = pygame.font.Font(None, 50)
    med_font = pygame.font.Font(None, 125)
    cur_ammo = font1.render(str(player.gun.current_ammo), True, (160, 0, 0))
    reload_num = font2.render(str(round(player.gun.reload / 60, 1)), True, (160, 0, 0))
    total_ammo = font1.render(str(player.gun.total_ammo), True, (160, 0, 0))
    hp = font1.render(str(player.hit_points), True, (160, 0, 0))
    medkits = med_font.render(str(player.medkits), True, (160, 0, 0))
    text_x = player.rect.x + 390
    text_y = player.rect.y + 310
    text_w = cur_ammo.get_width()
    text_h = cur_ammo.get_height()
    screen1.blit(HP_image, (50, HEIGHT - 150))
    screen1.blit(cur_ammo, (WIDTH - 140, text_y + 100))
    screen1.blit(total_ammo, (WIDTH - 140, text_y + 160))
    screen1.blit(medkits, (210, HEIGHT - 125))
    if player.gun.reload / 60 > 0.4:
        screen1.blit(reload_num, (player.rect.x + 10, player.rect.y + 100))
    for i in range(player.hit_points // 5):
        image1 = pygame.transform.scale(HP_piece_img, (20, 40))
        screen1.blit(image1, (100 + (i // 20) * 32, i % 20 * 40 + 75))
    if player.gun_num == 0:
        screen1.blit(pygame.transform.scale(guns_menu_images[0], (224, 72)), (WIDTH - 500, HEIGHT - 150))
    else:
        screen1.blit(pygame.transform.scale(guns_menu_images[1], (200, 96)), (WIDTH - 500, HEIGHT - 150))


class Marker(pygame.sprite.Sprite):
    def __init__(self, pl):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((0, 0))
        self.image.fill((100, 200, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.pl = pl

    def update(self):
        if self.rect.x > WIDTH:
            self.pl.rect.x += 5
        elif self.rect.x < - WIDTH:
            self.pl.rect.x -= 5
        if self.rect.y > HEIGHT:
            self.pl.rect.y += 5
        elif self.rect.y < - HEIGHT:
            self.pl.rect.y -= 5


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_stand = player_image
        self.image = self.image_stand
        self.image_run1 = player_run1
        self.image_run2 = player_run2
        all_sprites.add(self)
        self.images = [self.image_stand, self.image_run1, self.image_run2]
        self.image_num = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.guns = [Shotgun(2, self, shotgun_image, 0), Assault_rifle(3, self, rifle_image, 1)]
        all_sprites.add(self.guns[0], self.guns[1])
        self.gun = self.guns[0]
        self.gun_num = 0
        self.hit_points = 100
        self.medkits = 0
        self.change_sprite = 30
        self.shooting = False
        self.left = False
        self.moved = False
        self.collected = []
        self.multiplier = 1

    def update(self):
        self.multiplier = 1
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LSHIFT]:
            self.multiplier = 2
        if keystate[pygame.K_a]:
            self.speedx = -2 * self.multiplier
            self.left = True
            self.change_sprite -= 1 * self.multiplier
            self.moved = True
        if keystate[pygame.K_d]:
            self.speedx = 2 * self.multiplier
            self.left = False
            self.change_sprite -= 1 * self.multiplier
            self.moved = True
        if keystate[pygame.K_w]:
            self.speedy = -2 * self.multiplier
            self.change_sprite -= 1 * self.multiplier
            self.moved = True
        if keystate[pygame.K_s]:
            self.speedy = 2 * self.multiplier
            self.change_sprite -= 1 * self.multiplier
            self.moved = True
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.gun.reload != 0:
            self.gun.reload -= 1
        if self.shooting:
            if self.gun.reload == 0:
                self.shoot(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        if self.change_sprite <= 0:
            if self.image_num == 0:
                self.image = self.images[1]
                self.image_num = 1
            elif self.image_num == 1:
                self.image = self.images[2]
                self.image_num = 2
            elif self.image_num == 2:
                self.image = self.images[1]
                self.image_num = 1
            self.change_sprite = 30
        if not self.moved:
            self.image = self.images[0]
            self.image_num = 0
        self.moved = False
        if self.left:
            self.image = pygame.transform.flip(self.images[self.image_num], True, False)

    def change_weapon(self, num):
        self.gun = self.guns[num]
        self.gun_num = num

    def shoot(self, x, y):
        speedx = 10
        speedy = 10
        target_x = x - self.rect.x
        target_y = y - self.rect.y
        if target_y:
            target_xdely = target_x / target_y
        else:
            target_xdely = target_x / (target_y + 1)
        if target_y < 0:
            if target_xdely > 0.34 and target_xdely < 2.94:
                speedx = -10
                speedy = -10
            elif target_xdely > -0.34 and target_xdely < 0.34:
                speedx = 0
                speedy = -10
            elif target_xdely < 0.34 and target_xdely > -2.94:
                speedx = 10
                speedy = -10
            elif target_xdely < -2.94:
                speedx = 10
                speedy = 0
            elif target_xdely > 2.94:
                speedx = -10
                speedy = 0
        else:
            if target_xdely > 0.34 and target_xdely < 2.94:
                speedx = 10
                speedy = 10
            elif target_xdely > -0.34 and target_xdely < 0.34:
                speedx = 0
                speedy = 10
            elif target_xdely < 0.34 and target_xdely > -2.94:
                speedx = -10
                speedy = 10
            elif target_xdely < -2.94:
                speedx = -10
                speedy = 0
            elif target_xdely > 2.94:
                speedx = 10
                speedy = 0

        self.gun.shoot(self.rect.x + 32, self.rect.y + 60, speedx, speedy)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, pl):
        self.dx = 0
        self.dy = 0
        self.pl = pl

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self):
        self.dx = -(self.pl.rect.x + 32 - WIDTH // 2)
        self.dy = -(self.pl.rect.y + 48 - HEIGHT // 2)


def main_game(map):
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    global score
    running = True
    encoords = []
    player = Player()
    mark = Marker(player)
    all_sprites.add(mark)
    camera = Camera(player)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'b':
                m = Box(j * 100, i * 100, box_image, player)
                all_sprites.add(m)
                boxes.add(m)
            elif map[i][j][0] == 'e':
                encoords.append((j * 100, i * 100))
            elif map[i][j] == 'm':
                c = Medkit(j * 100, i * 100, medkit_image, player)
                all_sprites.add(c)
            elif map[i][j][0] == 'a':
                if map[i][j][1] == 'r':
                    c = Ammo_box(j * 100, i * 100, rifle_ammo, player, 'Rifle')
                    all_sprites.add(c)
                elif map[i][j][1] == 's':
                    c = Ammo_box(j * 100, i * 100, shotgun_ammo, player, 'Shotgun')
                    all_sprites.add(c)
            elif map[i][j][0] == 't':
                c = Text(j * 100, i * 100, text_image, player, map[i][j][1])
                all_sprites.add(c)
            elif map[i][j] == 'f':
                c = Signal_fire(j * 100, i * 100, fire_im[0], fire_im[1], player)
                fires.add(c)
                all_sprites.add(c)
    for i in encoords:
        c = Enemy(i[0], i[1], player, borsh_images)
        all_sprites.add(c)
        enemys.add(c)

    pygame.mixer.music.load('music/Soundtrack2.mp3')
    pygame.mixer.music.set_volume(0.025)
    pygame.mixer.music.play(loops=-1)

    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        hits = pygame.sprite.groupcollide(enemys, bullets, False, True, pygame.sprite.collide_rect)
        for hit in hits:
            hit.hit_points -= hits[hit][0].get_damage()

        if player.hit_points <= 0:
            running = False
            for e in all_sprites:
                e.kill()
            return [score[0], player.collected]

        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False
                for e in all_sprites:
                    e.kill()
                pygame.quit()
                return [score[0], player.collected]

            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shooting = True
            elif event.type == pygame.MOUSEBUTTONUP:
                player.shooting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player.change_weapon(0)
                if event.key == pygame.K_2:
                    player.change_weapon(1)
                if event.key == pygame.K_r:
                    player.gun.reload_ammo()
                if event.key == pygame.K_f:
                    if player.medkits > 0:
                        player.hit_points += 20
                        player.medkits -= 1
                if event.key == pygame.K_e:
                    for i in fires:
                        if pygame.sprite.collide_rect(i, player):
                            running = False
                            for e in all_sprites:
                                e.kill()
                            return [score[0] + 50, player.collected]

        all_sprites.update()
        camera.update()
        for sprite in all_sprites:
            camera.apply(sprite)

        screen.fill(BLACK)

        all_sprites.draw(screen)
        show_stats(player, screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()



box_image = pygame.image.load('Images/box.png').convert_alpha()
player_image = pygame.image.load('Images/player_stand.png').convert_alpha()
player_run1 = pygame.image.load('Images/player_run1.png').convert_alpha()
player_run2 = pygame.image.load('Images/player_run2.png').convert_alpha()
medkit_image = pygame.image.load('Images/medkit.png').convert_alpha()
shotgun_ammo = pygame.image.load('Images/shotgun_ammo.png').convert_alpha()
rifle_ammo = pygame.image.load('Images/ammo_rifle.png').convert_alpha()
shotgun_image = pygame.image.load('Images/shotgun_defolt.png').convert_alpha()
rifle_image = pygame.image.load('Images/rifle.png').convert_alpha()
text_image = pygame.image.load('Images/disckette.png').convert_alpha()
HP_image = pygame.image.load('Images/HP_menu.png').convert_alpha()
HP_piece_img = pygame.image.load('Images/HP_piece.png').convert_alpha()
borsh_1 = pygame.image.load('Images/борщевик1.png').convert_alpha()
borsh_2 = pygame.image.load('Images/борщевик2.png').convert_alpha()
borsh_3 = pygame.image.load('Images/борщевик3.png').convert_alpha()
fire_im = [pygame.image.load('Images/signal_fire.png').convert_alpha(),
           pygame.image.load('Images/signal_fire2.png').convert_alpha()]
guns_menu_images = [pygame.image.load('Images/shotgun_menu.png').convert_alpha(),
                    pygame.image.load('Images/rifle_menu.png').convert_alpha()]
borsh_images = [borsh_1, borsh_2, borsh_3]


pygame.quit()
