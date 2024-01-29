import os
from start_menu import startGame
from dotenv import load_dotenv
from player import Player
from world_generation import World
from game_objects import *
from button import Button
from support import createResult
from database import ScoreTable

# base
load_dotenv('.env')
pygame.init()
screen_size = (int(os.environ.get('WIDTH')), int(os.environ.get('HEIGHT')))
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
timer = pygame.time.Clock()

# input nickname
nickname = startGame(screen, background)

# flags
running = True
movement_right = 0
double_jump = False
game_status = "start"

# objects
player = Player(screen_size[0] // 2 - int(os.environ.get('PLAYER_WIDTH')) // 2,
                screen_size[1] - int(os.environ.get('PLAYER_HEIGHT')))
wall_width = int(os.environ.get('WALL_SIZE'))
wall_generation = World()

font = pygame.font.Font(None, 40)
restart_button = Button((0, 0, 0), 62, 150, 100, 30, 10, "Заново", (255, 0, 0))
exit_button = Button((0, 0, 0), 62, 190, 100, 30, 10, "Выйти", (255, 0, 0))
restart_button.changePos(62, 210)
exit_button.changePos(62, 250)
table = ScoreTable("results.db")
results_text = createResult(table)

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

        if game_status == 'start' and event.type == pygame.KEYDOWN \
                and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
            game_status = "duration"

        # movement
        if not double_jump and player.getX() > 30 \
                and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if movement_right != 0:
                double_jump = True
            movement_right = -1

        if not double_jump and player.getX() < screen_size[0] - 30 - int(os.environ.get("PLAYER_HEIGHT")) \
                and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if movement_right != 0:
                double_jump = True
            movement_right = 1

        # button
        if event.type == pygame.MOUSEBUTTONDOWN and (game_status == "dead" or game_status == "win"):
            if restart_button.pressed(pygame.mouse.get_pos()):
                game_status = "start"
                player = Player(screen_size[0] // 2 - int(os.environ.get('PLAYER_WIDTH')) // 2,
                                screen_size[1] - int(os.environ.get('PLAYER_HEIGHT')))
                wall_generation = World()
            if exit_button.pressed(pygame.mouse.get_pos()):
                running = False

    # start game
    if game_status == "start":
        for t, text in enumerate(start_texts):
            screen.blit(text, ((int(os.environ.get("WIDTH")) - text.get_width()) / 2, 70 + 20 * t))
        screen.blit(left_arrow, (130, 190))
        screen.blit(right_arrow, (76, 190))

    # process game
    if game_status == "duration":
        screen.blit(font.render(str(wall_generation.score), True, (0, 0, 0)), (100, 20))
        if not (is_win := player.update(movement_right, wall_generation.rectangles, wall_generation.isFinished())):
            game_status = "dead"
        if is_win == 2:
            game_status = "win"
            table.addScore(nickname=nickname, score=wall_generation.score)
            results_text = createResult(table)
        if movement_right:
            if player.getX() <= 30 or player.getX() >= screen_size[0] - 30 - int(os.environ.get("PLAYER_HEIGHT")):
                movement_right = 0
                double_jump = False
        wall_generation.draw(screen, player.getCollide())
        wall_generation.update()

    # win/dead
    if game_status == "win" or game_status == "dead":
        restart_button.update(screen)
        exit_button.update(screen)
        screen.blit(table_text, (60, 80))
        for t, text in enumerate(results_text):
            screen.blit(text, (45, 103 + t * 20))
    if game_status == "dead":
        screen.blit(dead_text, (62, 50))

    player.draw(screen)
    pygame.display.flip()

pygame.quit()
