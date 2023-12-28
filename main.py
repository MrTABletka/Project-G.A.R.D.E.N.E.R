import pygame
import random
import sys
from classes import Enemy, Bullet, Gun, all_sprites, bullets, enemys, Shotgun, Assault_rifle, score

WIDTH = 1000
HEIGHT = 800
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (100, 100, 75)
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

def show_ammo(player):
    font1 = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 50)
    text = font1.render(str(player.gun.current_ammo), True, (0, 0, 0))
    text2 = font2.render(str(round(player.gun.reload / 60, 1)), True, (0, 0, 0))
    text_x = player.rect.x + 200
    text_y = player.rect.y + 300
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    if player.gun.reload / 60 > 0.4:
        screen.blit(text2, (text_x - 200, text_y - 200))


class Marker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((0,0))
        self.image.fill((100, 200, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def update(self):
        if self.rect.x > WIDTH:
            player.rect.x += 5
        elif self.rect.x < - WIDTH:
            player.rect.x -= 5
        if self.rect.y > HEIGHT:
            player.rect.y += 5
        elif self.rect.y < - HEIGHT:
            player.rect.y -= 5




class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image_right = player_image
        self.left_image = pygame.transform.flip(player_image, True, False)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.guns = [Shotgun(2), Assault_rifle(3)]
        self.gun = self.guns[1]
        self.shooting = False

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -3
            self.image = self.left_image
        if keystate[pygame.K_d]:
            self.speedx = 3
            self.image = self.image_right
        if keystate[pygame.K_w]:
            self.speedy = -3
        if keystate[pygame.K_s]:
            self.speedy = 3
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

    def change_weapon(self, num):
        self.gun = self.guns[num]


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
                target = 'top_left'
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

        self.gun.shoot(self.rect.x + 32, self.rect.y + 48, speedx, speedy)

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self):
        self.dx = -(player.rect.x + 32 - WIDTH // 2)
        self.dy = -(player.rect.y + 48 - HEIGHT // 2)

def main_game():
    global score
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        hits = pygame.sprite.groupcollide(enemys, bullets, False, True, pygame.sprite.collide_rect)
        for hit in hits:
            hit.hit_points -= hits[hit][0].get_damage()

        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False
                return score[0]

            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shooting = True
            elif event.type == pygame.MOUSEBUTTONUP:
                player.shooting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player.change_weapon(0)
                if event.key == pygame.K_2:
                    player.change_weapon(1)
        all_sprites.update()
        camera.update()
        for sprite in all_sprites:
            camera.apply(sprite)

        # Обновление

        # Рендеринг
        screen.fill(BLACK)

        all_sprites.draw(screen)
        show_ammo(player)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()


camera = Camera()
player_image = pygame.image.load('player_stand.png').convert_alpha()
player = Player()
mark = Marker()
all_sprites.add(mark)
all_sprites.add(player)
for i in range(8):
    m = Enemy()
    all_sprites.add(m)
    enemys.add(m)
print(main_game())
pygame.quit()
#hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
#hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)