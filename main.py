import pygame
import random

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
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = speedy
        self.speedx = speedx

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0

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
        target_xdely = target_x / target_y
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


        bullet = Bullet(self.rect.x + 25, self.rect.y + 25, speedx, speedy)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, 600)


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()
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