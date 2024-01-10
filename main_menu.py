import pygame
import sys
from main import main_game

pygame.init()

screen_width = 1024
screen_height = 576

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Меню игры")

background_image = pygame.image.load("background.png")
button_raid_image = pygame.image.load("buttons_raid.png")
button_newgame_image = pygame.image.load("buttons_newgame.png")
button_uprav_image = pygame.image.load("buttons_uprav.png")
button_shop_image = pygame.image.load("buttons_shop.png")
button_zapis_image = pygame.image.load("buttons_zapis.png")
button_stats_image = pygame.image.load("buttons_stats.png")
button_exit_image = pygame.image.load("buttons_exit.png")

button_raid_image = pygame.transform.scale(button_raid_image, (button_raid_image.get_width() / 7, button_raid_image.get_height() / 7))
button_newgame_image = pygame.transform.scale(button_newgame_image, (button_newgame_image.get_width() / 7, button_newgame_image.get_height() / 7))
button_uprav_image = pygame.transform.scale(button_uprav_image, (button_uprav_image.get_width() / 7, button_uprav_image.get_height() / 7))
button_shop_image = pygame.transform.scale(button_shop_image, (button_shop_image.get_width() / 7, button_shop_image.get_height() / 7))
button_zapis_image = pygame.transform.scale(button_zapis_image, (button_zapis_image.get_width() / 7, button_zapis_image.get_height() / 7))
button_stats_image = pygame.transform.scale(button_stats_image, (button_stats_image.get_width() / 7, button_stats_image.get_height() / 7))
button_exit_image = pygame.transform.scale(button_exit_image, (button_exit_image.get_width() / 7, button_exit_image.get_height() / 7))

button_raid_pos = (screen_width // 2 - button_raid_image.get_width() // 2, 10)
button_newgame_pos = (screen_width // 3 - button_newgame_image.get_width() // 2, 150)
button_uprav_pos = (screen_width // 1.5 - button_uprav_image.get_width() // 2, 150)
button_shop_pos = (screen_width // 3 - button_shop_image.get_width() // 2, 275)
button_zapis_pos = (screen_width // 1.5 - button_zapis_image.get_width() // 2, 275)
button_stats_pos = (screen_width // 3 - button_stats_image.get_width() // 2, 400)
button_exit_pos = (screen_width // 1.5 - button_exit_image.get_width() // 2, 400)

button_scale = 1.0
hovered_button = None
background_x = 0


def check_button_hover(pos, button_pos, button_image):
    if (button_pos[0] <= pos[0] <= button_pos[0] + button_image.get_width() and
            button_pos[1] <= pos[1] <= button_pos[1] + button_image.get_height()):
        return True
    return False


a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if check_button_hover(mouse_pos, button_raid_pos, button_raid_image):
                hovered_button = "raid"
            elif check_button_hover(mouse_pos, button_newgame_pos, button_newgame_image):
                hovered_button = "newgame"
            elif check_button_hover(mouse_pos, button_uprav_pos, button_uprav_image):
                hovered_button = "uprav"
            elif check_button_hover(mouse_pos, button_shop_pos, button_shop_image):
                hovered_button = "shop"
            elif check_button_hover(mouse_pos, button_zapis_pos, button_zapis_image):
                hovered_button = "zapis"
            elif check_button_hover(mouse_pos, button_stats_pos, button_stats_image):
                hovered_button = "stats"
            elif check_button_hover(mouse_pos, button_exit_pos, button_exit_image):
                hovered_button = "exit"
            else:
                hovered_button = None
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if check_button_hover(mouse_pos, button_raid_pos, button_raid_image):
                carta = [['v', 'b', 'e', 'ar', 'v', 'v', 'b', 'e'], ['v', 'b', 'e', 'as', 'm', 't1', 'b', 'e'], ['t3']]
                print(main_game(carta))
                a = False

    background_x -= 2
    if background_x < -background_image.get_width():
        background_x = 0

    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_image.get_width(), 0))

    if hovered_button == "raid":
        button_raid_image_scaled = pygame.transform.scale(button_raid_image, (int(button_raid_image.get_width() * 1.1), int(button_raid_image.get_height() * 1.1)))
        screen.blit(button_raid_image_scaled, button_raid_pos)
    else:
        screen.blit(button_raid_image, button_raid_pos)

    if hovered_button == "newgame":
        button_newgame_image_scaled = pygame.transform.scale(button_newgame_image, (int(button_newgame_image.get_width() * 1.1), int(button_newgame_image.get_height() * 1.1)))
        screen.blit(button_newgame_image_scaled, button_newgame_pos)
    else:
        screen.blit(button_newgame_image, button_newgame_pos)

    if hovered_button == "uprav":
        button_uprav_image_scaled = pygame.transform.scale(button_uprav_image, (int(button_uprav_image.get_width() * 1.1), int(button_uprav_image.get_height() * 1.1)))
        screen.blit(button_uprav_image_scaled, button_uprav_pos)
    else:
        screen.blit(button_uprav_image, button_uprav_pos)

    if hovered_button == "shop":
        button_shop_image_scaled = pygame.transform.scale(button_shop_image, (int(button_shop_image.get_width() * 1.1), int(button_shop_image.get_height() * 1.1)))
        screen.blit(button_shop_image_scaled, button_shop_pos)
    else:
        screen.blit(button_shop_image, button_shop_pos)

    if hovered_button == "zapis":
        button_zapis_image_scaled = pygame.transform.scale(button_zapis_image, (int(button_zapis_image.get_width() * 1.1), int(button_zapis_image.get_height() * 1.1)))
        screen.blit(button_zapis_image_scaled, button_zapis_pos)
    else:
        screen.blit(button_zapis_image, button_zapis_pos)

    if hovered_button == "stats":
        button_stats_image_scaled = pygame.transform.scale(button_stats_image, (int(button_stats_image.get_width() * 1.1), int(button_stats_image.get_height() * 1.1)))
        screen.blit(button_stats_image_scaled, button_stats_pos)
    else:
        screen.blit(button_stats_image, button_stats_pos)

    if hovered_button == "exit":
        button_exit_image_scaled = pygame.transform.scale(button_exit_image, (int(button_exit_image.get_width() * 1.1), int(button_exit_image.get_height() * 1.1)))
        screen.blit(button_exit_image_scaled, button_exit_pos)
    else:
        screen.blit(button_exit_image, button_exit_pos)

    if a:
        pygame.display.flip()


