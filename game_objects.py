import pygame

pygame.init()
background = pygame.image.load("sprites/background.png")
left_arrow = pygame.image.load("sprites/arrow.png")
right_arrow = pygame.transform.flip(left_arrow, True, False)

# texts
# nickname input
font = pygame.font.Font(None, 28)
text_input_1 = font.render("Привет герой!", True, (0, 0, 0))
text_input_2 = font.render("Введи своё имя!", True, (0, 0, 0))

# dead menu
font = pygame.font.Font(None, 32)
dead_text = font.render("Ты умер!", True, (255, 0, 0))

# start menu
font = pygame.font.Font(None, 24)
start_texts = [
    font.render("Доберись до", True, (0, 0, 0)),
    font.render("самого конца!", True, (0, 0, 0)),
    font.render("Собери как можно ", True, (0, 0, 0)),
    font.render("больше монет!", True, (0, 0, 0)),
    font.render("Чтобы начать", True, (0, 0, 0)),
    font.render("нажмите", True, (0, 0, 0)),
]

# win menu
font = pygame.font.Font(None, 24)
table_text = font.render("Результаты: ", True, (0, 0, 0))
