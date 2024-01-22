import pygame
import sys
from main import main_game, Player
import random


screen_width = 1920
screen_height = 1080


def menu():
    player = Player()
    global b
    screen = pygame.display.set_mode((screen_width, screen_height),
                                     pygame.FULLSCREEN)
    pygame.display.set_caption("Меню игры")
    pygame.mixer.init()
    pygame.mixer.music.load('music/menu_music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    level_passed = pygame.image.load("level_passed.png")
    level_died = pygame.image.load("level_died.png")
    background_final_success = pygame.image.load("background_final_success.png")
    background_final_died = pygame.image.load("background_final_died.png")
    background_image = pygame.image.load("background.png")
    button_play_image = pygame.image.load("buttons_play.png")
    button_uprav_image = pygame.image.load("buttons_uprav.png")
    button_authors_image = pygame.image.load("buttons_authors.png")
    button_exit_image = pygame.image.load("buttons_exit.png")
    controls_image = pygame.image.load("controls.png")
    button_back_image = pygame.image.load("buttons_back.png")
    authors_image = pygame.image.load("authors.png")


    background_image = pygame.transform.scale(background_image,
                                               (
                                               background_image.get_width() * 1.8,
                                               background_image.get_height() * 1.8))


    button_play_image = pygame.transform.scale(button_play_image,
                                               (
                                               button_play_image.get_width() * 1.4,
                                               button_play_image.get_height()* 1.4))

    button_uprav_image = pygame.transform.scale(button_uprav_image,
                                                (
                                                button_uprav_image.get_width(),
                                                button_uprav_image.get_height()))

    button_authors_image = pygame.transform.scale(button_authors_image,
                                                (
                                                button_authors_image.get_width(),
                                                button_authors_image.get_height()))

    button_exit_image = pygame.transform.scale(button_exit_image,
                                               (
                                               button_exit_image.get_width(),
                                               button_exit_image.get_height()))
    controls_image = pygame.transform.scale(controls_image,
                                               (
                                               controls_image.get_width() * 1.5,
                                               controls_image.get_height() * 1.5))
    button_back_image = pygame.transform.scale(button_back_image,
                                               (
                                               button_back_image.get_width(),
                                               button_back_image.get_height()))
    authors_image = pygame.transform.scale(authors_image,
                                               (
                                               authors_image.get_width() * 1.5,
                                               authors_image.get_height() * 1.5))
    background_final_success = pygame.transform.scale(background_final_success,
                                               (
                                               background_final_success.get_width() * 1.8,
                                               background_final_success.get_height() * 1.8))


    button_play_pos = (
    screen_width // 2 - button_play_image.get_width() // 2, 50)
    button_uprav_pos = (
    screen_width // 2 - button_uprav_image.get_width() // 2, 400)
    button_authors_pos = (
    screen_width // 3 - button_authors_image.get_width() // 2, 650)
    button_exit_pos = (
    screen_width // 1.5 - button_exit_image.get_width() // 2, 650)
    controls_pos = (
    screen_width // 2 - controls_image.get_width() // 2, 1750)
    button_back_pos = (
    screen_width // 1.5 - button_back_image.get_width() // 2, 1750)
    authors_image_pos = (
    screen_width // 1.5 - authors_image.get_width() // 2, 1500)

    button_scale = 1.0
    hovered_button = None
    background_x = 0
    player = Player()

    if player.died:
        screen.blit(background_final_died, (0, 0))
        screen.blit(level_died, (
        screen_width // 2 - level_died.get_width() // 2, screen_height // 2 - level_died.get_height() // 2))
    else:
        background_x = 0

    pygame.init()
    a = True
    if player.died:
        background_final_success = pygame.image.load("background_final_died.png")
        level_image = pygame.image.load("level_died.png")
    elif player.captured:
        background_final_image = pygame.image.load("background_final_success.png")
        level_image = pygame.image.load("level_passed.png")
    while a:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                if check_button_hover(mouse_pos, button_play_pos, button_play_image):
                    hovered_button = "play"
                elif check_button_hover(mouse_pos, button_uprav_pos, button_uprav_image):
                    hovered_button = "uprav"
                elif check_button_hover(mouse_pos, button_authors_pos, button_authors_image):
                    hovered_button = "authors"
                elif check_button_hover(mouse_pos, button_exit_pos, button_exit_image):
                    hovered_button = "exit"
                elif check_button_hover(mouse_pos, controls_pos, controls_image):
                    hovered_button = "controls"
                elif check_button_hover(mouse_pos, button_back_pos, button_back_image):
                    hovered_button = "back"
                elif check_button_hover(mouse_pos, authors_image_pos, authors_image):
                    hovered_button = "authors"
                else:
                    hovered_button = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if check_button_hover(mouse_pos, button_play_pos, button_play_image):
                    carta1 = [
                        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
                         'b'],
                        ['b', 'as', 'm', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'b', 'm', 'v', 'e', 'v', 'v', 'e', 'v', 'v',
                         'ar', 'b'],
                        ['b', 'v', 'e', 'v', 'b', 'v', 'v', 'v', 'v', 'v', 'b', 'v', 'b', 'b', 'b', 'b', 'b', 'v', 'v', 'e',
                         'b'],
                        ['b', 'ar', 'e', 'v', 'b', 'v', 'v', 'v', 'v', 'v', 'b', 'v', 'e', 'v', 't4', 'e', 'e', 'v', 'v',
                         'v', 'b'],
                        ['b', 'b', 'b', 'b', 'b', 't1', 'v', 'v', 'v', 'v', 'b', 'v', 'b', 'b', 'b', 'b', 'b', 'v', 'v',
                         'ar', 'b'],
                        ['b', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'b', 'v', 'v', 'e', 'v', 'v', 'v', 'v', 'e', 'v',
                         'b'],
                        ['b', 'v', 'e', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'b', 'v', 'v', 'v', 'v', 'v', 'f', 'v', 'v', 'e',
                         'b'],
                        ['b', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'b', 'v', 'v', 'v', 'v', 'e', 'v', 'v', 'v',
                         'as', 'b'],
                        ['b', 'b', 'b', 'b', 'b', 'b', 'v', 'v', 'v', 'e', 'v', 'e', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v',
                         'b'],
                        ['b', 'ar', 'v', 'v', 'v', 'b', 'v', 'v', 'v', 'v', 'v', 'b', 'b', 'b', 'v', 'v', 'b', 'b', 'b',
                         'b', 'b'],
                        ['b', 'v', 'as', 'e', 'm', 'v', 'v', 'v', 'v', 'v', 'v', 'b', 'e', 'v', 'v', 'v', 'b', 'v', 'v',
                         't3', 'b'],
                        ['b', 'v', 'v', 'v', 'v', 'e', 'v', 'v', 'v', 'v', 'e', 'b', 'm', 'v', 'b', 'b', 'b', 'v', 'm', 'e',
                         'b'],
                        ['b', 'e', 'v', 'v', 'v', 'b', 'v', 't2', 'v', 'e', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'e', 'as',
                         'e', 'b'],
                        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
                         'b']
                        ]
                    carta2 = [['b', 'v', 'v', 'v', 'v', 'b', 'v', 'b', 'v', 'b', 'v', ],
                              ['b', 'as', 'ar', 'm', 't1', 'v', 'v', 'v', 'v', 'e', 'v'],
                              ['b', 'v', 'v', 'v', 'v', 'm', 'e', 'b', 'v', 'b', 'v'],
                              ['b', 'm', 'f', 'v', 'v', 'm', 'e', 'v', 'm', 'm', 'm'],
                              ]
                    if random.randrange(0, 2, step=1):
                        print(main_game(carta1))

                    else:
                        print(main_game(carta2))
                    a = False
                if check_button_hover(mouse_pos, button_uprav_pos, button_uprav_image):
                    button_play_pos = (
                        screen_width // 2 - button_play_image.get_width() // 2, 1200)
                    button_uprav_pos = (
                        screen_width // 2 - button_uprav_image.get_width() // 2, 1525)
                    button_authors_pos = (
                        screen_width // 3 - button_authors_image.get_width() // 2, 1750)
                    button_exit_pos = (
                        screen_width // 1.5 - button_exit_image.get_width() // 2, 1750)
                    controls_pos = (
                        screen_width // 2 - controls_image.get_width() // 2, 100)
                    button_back_pos = (
                        screen_width // 6 - button_back_image.get_width() // 2, 300)

                if check_button_hover(mouse_pos, button_back_pos, button_back_image):
                    button_play_pos = (
                        screen_width // 2 - button_play_image.get_width() // 2, 50)
                    button_uprav_pos = (
                        screen_width // 2 - button_uprav_image.get_width() // 2, 400)
                    button_authors_pos = (
                        screen_width // 3 - button_authors_image.get_width() // 2, 650)
                    button_exit_pos = (
                        screen_width // 1.5 - button_exit_image.get_width() // 2, 650)
                    controls_pos = (
                        screen_width // 2 - controls_image.get_width() // 2, 1750)
                    button_back_pos = (
                        screen_width // 1.5 - button_back_image.get_width() // 2, 1750)
                    authors_image_pos = (
                        screen_width // 2 - controls_image.get_width() // 2, 1500)

                if check_button_hover(mouse_pos, button_authors_pos, button_authors_image):
                    button_play_pos = (
                        screen_width // 2 - button_play_image.get_width() // 2, 1200)
                    button_uprav_pos = (
                        screen_width // 2 - button_uprav_image.get_width() // 2, 1525)
                    button_authors_pos = (
                        screen_width // 3 - button_authors_image.get_width() // 2, 1750)
                    button_exit_pos = (
                        screen_width // 1.5 - button_exit_image.get_width() // 2, 1750)
                    authors_image_pos = (
                        screen_width // 2 - controls_image.get_width() // 2, 100)
                    button_back_pos = (
                        screen_width // 6 - button_back_image.get_width() // 2, 300)


                if check_button_hover(mouse_pos, button_exit_pos,
                                      button_exit_image):
                    b = False
                    pygame.quit()
                    sys.exit()

        if a:
            background_x -= 2
            if background_x < -background_image.get_width():
                background_x = 0

            screen.blit(background_image, (background_x, 0))
            screen.blit(background_image, (background_x + background_image.get_width(), 0))

            if hovered_button == "play":
                button_play_image_scaled = pygame.transform.scale(button_play_image, (
                int(button_play_image.get_width() * 1.1), int(button_play_image.get_height() * 1.1)))
                screen.blit(button_play_image_scaled, button_play_pos)
            else:
                screen.blit(button_play_image, button_play_pos)

            if hovered_button == "uprav":
                button_uprav_image_scaled = pygame.transform.scale(button_uprav_image, (
                int(button_uprav_image.get_width() * 1.1), int(button_uprav_image.get_height() * 1.1)))
                screen.blit(button_uprav_image_scaled, button_uprav_pos)
            else:
                screen.blit(button_uprav_image, button_uprav_pos)

            if hovered_button == "authors":
                button_authors_image_scaled = pygame.transform.scale(button_authors_image, (
                int(button_authors_image.get_width() * 1.1), int(button_authors_image.get_height() * 1.1)))
                screen.blit(button_authors_image_scaled, button_authors_pos)
            else:
                screen.blit(button_authors_image, button_authors_pos)

            if hovered_button == "exit":
                button_exit_image_scaled = pygame.transform.scale(button_exit_image, (
                int(button_exit_image.get_width() * 1.1), int(button_exit_image.get_height() * 1.1)))
                screen.blit(button_exit_image_scaled, button_exit_pos)
            else:
                screen.blit(button_exit_image, button_exit_pos)

            if hovered_button == "controls":
                controls_image_scaled = pygame.transform.scale(controls_image, (
                int(controls_image.get_width() * 1), int(controls_image.get_height() * 1)))
                screen.blit(controls_image_scaled, controls_pos)
            else:
                screen.blit(controls_image, controls_pos)

            if hovered_button == "back":
                button_back_image_scaled = pygame.transform.scale(button_back_image, (
                int(button_back_image.get_width() * 1.1), int(button_back_image.get_height() * 1.1)))
                screen.blit(button_back_image_scaled, button_back_pos)
            else:
                screen.blit(button_back_image, button_back_pos)

            if hovered_button == "authors":
                authors_image_scaled = pygame.transform.scale(authors_image, (
                int(authors_image.get_width() * 1), int(authors_image.get_height() * 1)))
                screen.blit(authors_image_scaled, authors_image_pos)
            else:
                screen.blit(authors_image, authors_image_pos)

            if a:
                pygame.display.flip()
            if not a:
                pygame.quit()


def check_button_hover(pos, button_pos, button_image):
    if (button_pos[0] <= pos[0] <= button_pos[0] + button_image.get_width() and
            button_pos[1] <= pos[1] <= button_pos[1] + button_image.get_height()):
        return True
    return False


b = True
while True:
    b = True
    pygame.init()
    while b:
        menu()
