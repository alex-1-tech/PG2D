import pygame

class Button:
    # create Button class
    def __init__(self, color, x, y, length, height, width, text, text_color):
        self._color = color
        self._x = x
        self._y = y
        self._length = length
        self._height = height
        self._width = width
        self._text = text
        self._text_color = text_color
        self._rect = pygame.Rect(self._x, self._y, self._length, self._height)

    def writeText(self, surface):
        font_size = 20
        my_font = pygame.font.SysFont("Calibri", font_size)
        my_text = my_font.render(self._text, True, self._text_color)
        surface.blit(my_text, (
        (self._x + self._length / 2) - my_text.get_width() / 2, (self._y + self._height / 2) - my_text.get_height() / 2))

    def drawButton(self, surface):
        pygame.draw.rect(surface, self._color, (self._x, self._y, self._length, self._height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (self._x, self._y, self._length, self._height), 1)

    def update(self, screen):
        self.drawButton(screen)
        self.writeText(screen)

    def pressed(self, mouse):
        if self._rect.topleft[0] < mouse[0] < self._rect.bottomright[0] \
                and self._rect.topleft[1] < mouse[1] < self._rect.bottomright[1]:
            return True
        return False

    def changePos(self, x, y):
        self._x = x
        self._y = y
        self._rect = pygame.Rect(self._x, self._y, self._length, self._height)