import os
import pygame
from dotenv import load_dotenv
from player import Player
from world_generation import World

# base
load_dotenv('.env')
screen_size = (int(os.environ.get('WIDTH')), int(os.environ.get('HEIGHT')))
pygame.init()
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
timer = pygame.time.Clock()

# sprites
background = pygame.image.load("sprites/background.png")

# flags
running = True
movement_right = 0
double_jump = False

# objects
player = Player(screen_size[0] // 2 - int(os.environ.get('PLAYER_WIDTH')) // 2,
                screen_size[1] - int(os.environ.get('PLAYER_HEIGHT')))
wall_width = int(os.environ.get('WALL_SIZE'))
wall_generation = World()
score = 0

while running:
    # draw the main environment
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0),
                     (0, 0, wall_width, screen_size[1]))
    pygame.draw.rect(screen, (0, 0, 0),
                     (screen_size[0] - wall_width, 0, screen_size[0], screen_size[1]))
    timer.tick(140)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not double_jump and player.getX() > 30 \
                and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if movement_right != 0:
                double_jump = True
            movement_right = -1

        if not double_jump and player.getX() < screen_size[0] - 30 - 22 \
                and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if movement_right != 0:
                double_jump = True
            movement_right = 1

    running = player.update(movement_right, wall_generation.rectangles)
    if movement_right:
        if player.getX() <= 30 or player.getX() >= screen_size[0] - 30 - 22:
            movement_right = 0
            double_jump = False

    wall_generation.draw(screen)
    wall_generation.update()
    player.draw(screen)
    pygame.display.flip()
