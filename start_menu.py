import sys
from game_objects import *
import pygame


def startGame(screen, background) -> str:
    nickname = ''
    input_box = pygame.Rect(25, 120, 180, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        nickname = nickname[:-1]
                    else:
                        nickname += event.unicode

        screen.blit(text_input_1, (48, 70))
        screen.blit(text_input_2, (38, 90))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(font.render(nickname, True, (0, 0, 0)), (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
    return nickname
