import pygame
import random
from classes import Enemy, Bullet, Gun, all_sprites, bullets, enemys, Shotgun

WIDTH = 600
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.gun = Shotgun(2)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_s]:
            self.speedy = 5
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

    def shoot(self, x, y):
        speedx = 10
        speedy = 10
        target_x = x - self.rect.x
        target_y = y - self.rect.y
        if target_y:
            target_xdely = target_x / target_y
        else:
            target_xdely = target_x / target_y + 1
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

        self.gun.shoot(self.rect.x + 25, self.rect.y + 25, speedx, speedy)


player = Player()
all_sprites.add(player)
for i in range(8):
    m = Enemy()
    all_sprites.add(m)
    enemys.add(m)
# Цикл игры
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot(event.pos[0], event.pos[1])

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
#hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
#hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)