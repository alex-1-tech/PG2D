import pygame
import sys
import random
import os


class Button:
    # create Button class
    def __init__(self, color, x, y, length, height, width, text, text_color):
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self._rect = pygame.Rect(x, y, length, height)

    def write_text(self, surface):
        font_size = 20
        my_font = pygame.font.SysFont("Calibri", font_size)
        my_text = my_font.render(self.text, True, self.text_color)
        surface.blit(my_text, (
        (self.x + self.length / 2) - my_text.get_width() / 2, (self.y + self.height / 2) - my_text.get_height() / 2))

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.length, self.height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (self.x, self.y, self.length, self.height), 1)

    def update(self, screen):
        self.draw_button(screen)
        self.write_text(screen)

    def pressed(self, mouse):
        if self._rect.topleft[0] < mouse[0] < self._rect.bottomright[0] \
                and self._rect.topleft[1] < mouse[1] < self._rect.bottomright[1]:
            return True
        return False
